# flake8: noqa
import json
from golismero3.engine import Engine
from golismero3.facts import Vector

# XXX Temp
from pyknow import *


GolismeroEngine = Engine.from_rulesets({
    "domain_scan": {
        "dns_resolver": {
            "lhs": [Vector(_type="domain", domain=MATCH.domain)],
            "command": "docker run -i golismero-plugin-dns-resolver:1.0.0"},
#        "harvester": {
#            "lhs": [Vector(_type="domain", domain=MATCH.domain)],
#            "command": "docker run -i golismero-plugin-harvester:1.0.0"},
    }})

watch("RULES", "FACTS")
engine = GolismeroEngine()

initial_vectors = [Vector(_type="domain", _id="lalala", domain="elpais.com")]

result = engine.start(vectors=initial_vectors)
print(json.dumps(list(result), indent=2))
