import operator as op
from functools import reduce

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
        for vector in vectors:
            vector["_lineage"] = list()
            yield vector

    @Rule(
        AS.info << Info(
            _id=MATCH.id,
            _type=NE("error") & MATCH.type),
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
        lineage = unfreeze(task["lineages"])
        stdin = unfreeze(task["stdin"])

        self.tasks.append(runner(lineage, stdin))

    def start(self, vectors):
        # Declare initial facts
        self.reset(vectors=vectors)

        fresh_facts = True
        while self.tasks or fresh_facts:
            self.run()
            fresh_facts = False

            try:
                # Run all tasks and gather results
                for task in self.tasks:
                    for lineage in task:
                        info = Info.from_lineage(lineage)
                        self.declare(info)
                        fresh_facts = True
            except KeyboardInterrupt:
                # The user aborted the task
                break

            self.tasks = list()

        # Print a dirty report
        for fact in self.facts.values():
            if isinstance(fact, Info):
                yield unfreeze(fact.as_dict())
