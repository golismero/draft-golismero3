import json
import os.path as op

from unittest.mock import MagicMock

from ..plugin_executor import main

HERE = op.dirname(__file__)


def test_plugin_dns_resolver_successful(monkeypatch):

    def fake(domain, register_type):
        a = MagicMock()
        a.items = []
        b = MagicMock()
        b.response.answer = [a]
        d = MagicMock()

        if register_type in ("A", "AAAA"):
            d.address = "127.0.0.1"
        elif register_type == "NS":
            d.target = "ns2.google.com"
        elif register_type == "MX":
            d.exchange = "mx1.google.com."
        else:
            raise ValueError("Unknown DNS type")

        a.items.append(d)

        return b

    monkeypatch.setattr('sys.stdin', op.join(HERE, "input_example.json"))
    monkeypatch.setattr('dns.resolver.query', fake)

    result = main()
    output_json = json.loads(result)

    for object_data in output_json:
        assert len(object_data) == 2
        assert object_data[0]['_type'] == 'ip'
        assert object_data[1]['_type'] in ('A', 'AAAA', 'MX', 'NS')

        assert "ip" in object_data[0]
        assert "value" in object_data[1]

