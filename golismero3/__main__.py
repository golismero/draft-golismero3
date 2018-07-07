from golismero3.engine import Engine
from golismero3.facts import Vector

# XXX Temp
from pyknow import *


GolismeroEngine = Engine.from_rulesets({
    "webscan": {
        "rule1": {"lhs": [Vector(_type="ip", ip=MATCH.dst)],
                  "command": "cat /home/nil/Project/golismero3/examples/tool_output.json"},
        "rule2": {"lhs": [Vector(_type="domain", domain=MATCH.dst),
                          Vector(_type="port", port=MATCH.port)],
                  "command": "command1.exe"},
        "rule3": {"lhs": [Vector(_type="port", port=MATCH.port)],
                  "command": "command2.exe"}}})

watch("RULES", "FACTS")
engine = GolismeroEngine()
engine.start(vectors=[Vector(_type="ip", _id="lalala", ip="192.168.1.1")])
