from pyknow import Fact
from pyknow.utils import unfreeze
from pprint import pformat


class PPrintFact(Fact):
    def __repr__(self):
        return f"\n{self.__class__.__name__}(\n{pformat(unfreeze(self.as_dict()), width=120)})"


class Vector(PPrintFact):
    """Vector to analyze"""
    pass


class Info(PPrintFact):
    """Discovered information"""
    @classmethod
    def from_lineage(cls, lineage):
        values = {"_lineage": lineage[:-1]}
        for item in lineage:
            values.update(item)
        return cls(**values)


class TaskRequest(PPrintFact):
    pass
