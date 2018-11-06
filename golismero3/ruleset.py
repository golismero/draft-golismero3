import operator as op
from functools import reduce

from pyknow import Rule, W, TEST

from golismero3.facts import TaskRequest


def _shared_lineage(**context):
    lineages = [v for k, v in context.items() if k.startswith("_lineage_")]
    items = [{(v["_id"], v["_type"]) for v in lineage} for lineage in lineages]
    if items:
        return bool(reduce(op.and_, items))
    else:
        return True


class RuleSet:
    @classmethod
    def build(cls, setname, spec):
        """
        Rule struct example
        {'rulename1': {'lhs': [Vector(_type="ip", ip=MATCH.pollas)))],
                       'command': "run_nmap.py"}}
        """
        def _create_rhs(command):
            def _rhs(self, **context):
                idxs = sorted([int(k.split('_')[2])
                               for k in context.keys()
                               if k.startswith('_elem_')],
                              reverse=True)
                lineages = list()
                for idx in idxs:
                    lineages.extend(context[f'_lineage_{idx}'])
                    elem = context[f'_elem_{idx}'].as_dict()
                    del elem['_lineage']
                    lineages.append(elem)

                stdin = {k: v
                         for k, v in context.items()
                         if not k.startswith("_")}

                self.declare(TaskRequest(command=command,
                                         stdin=stdin,
                                         lineages=lineages))
            return _rhs

        rules = {}
        for rulename, body in spec.items():
            comps = list()
            for idx, comp in enumerate(body['lhs']):
                comp["_lineage"] = W(f"_lineage_{idx}")
                f"_elem_{idx}" << comp
                comps.append(comp)
            lhs = Rule(*comps,
                       TEST(_shared_lineage))
            rhs = _create_rhs(body['command'])
            rhs.__name__ = f"{setname}__{rulename}"
            rules[rulename] = lhs(rhs)

        return type(setname, (cls,), rules)
