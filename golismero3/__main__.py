from golismero3.engine import Engine
from golismero3.facts import Vector

# XXX Temp
from pyknow import *


GolismeroEngine = Engine.from_rulesets({
    "webscan": {
        "rule1": {"lhs": Rule(Vector(type="ip", ip=MATCH.dst)),
                  "command": "command1.exe"},
        "rule2": {"lhs": Rule(Vector(type="domain", domain=MATCH.dst)),
                  "command": "command1.exe"}}})

watch("RULES", "FACTS")
engine = GolismeroEngine()
engine.start(vectors=[Vector(type="ip", ip="192.168.1.1")])
