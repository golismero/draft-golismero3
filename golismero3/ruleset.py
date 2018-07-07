from golismero3.facts import TaskRequest


class RuleSet:
    @classmethod
    def build(cls, name, spec):
        """
        Rule struct example
        {'rulename1': {'lhs': Rule(Vector(_type="ip", ip=MATCH.pollas))),
                       'command': "run_nmap.py"}}
        """
        def _create_rhs(command):
            def _rhs(self, **stdin):
                self.declare(TaskRequest(command=command, stdin=stdin))
            return _rhs

        rules = {}
        for rulename, body in spec.items():
            rules[rulename] = body['lhs'](_create_rhs(body['command']))

        return type(name, (cls,), rules)
