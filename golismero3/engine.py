from pyknow import *
from pyknow.utils import unfreeze
from golismero3.facts import Vector, Info, TaskRequest
from golismero3.ruleset import RuleSet
from golismero3.plugin import plugin_runner


class Engine(KnowledgeEngine):
    @classmethod
    def from_rulesets(cls, rulesets):
        mixins = list()
        for name, ruleset in rulesets.items():
            mixins.append(RuleSet.build(name, ruleset))

        return type("RuleEngine", tuple([cls] + mixins), {})

    @DefFacts()
    def initial_vector(self, vectors):
        self.tasks = list()
        yield from vectors

    @Rule(
        AS.info << Info(
            _id=MATCH.id,
            _type=MATCH.type),
        NOT(
            Vector(
                _id=MATCH.id,
                _type=MATCH.type)))
    def info_to_vector_promotion(self, info):
        """New vector appeared."""
        self.declare(Vector(**info.as_dict()))

    @Rule(
        AS.task << TaskRequest())
    def launch_task(self, task):
        runner = plugin_runner(task["command"])
        self.tasks.append(runner(unfreeze(task["stdin"])))

    def start(self, vectors):
        # Declare initial facts
        self.reset(vectors=vectors)

        first_run = True
        while self.tasks or first_run:
            first_run = False

            self.run()
            # Run all tasks and gather results
            for task in self.tasks:
                for lineage in task:
                    info = Info.from_lineage(lineage)
                    self.declare(info)
            self.tasks = list()
