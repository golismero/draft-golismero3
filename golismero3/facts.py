from pyknow import Fact


class Vector(Fact):
    """Vector to analyze"""
    pass


class Info(Fact):
    """Discovered information"""
    @classmethod
    def from_lineage(cls, lineage):
        values = dict()
        for item in lineage:
            values.update(item)
        return cls(**values)


class TaskRequest(Fact):
    pass
