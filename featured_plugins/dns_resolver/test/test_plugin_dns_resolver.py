import json
import os.path as op

from ..task import main

HERE = op.dirname(__file__)


def test_plugin_dns_resolver_successful(monkeypatch):

    monkeypatch.setattr('sys.stdin', op.join(HERE, "input_example.json"))

    result = main()
    output_json = json.loads(result)

    for object_data in output_json:
        assert '_id' in object_data
        assert '_type' in object_data
        assert 'value' in object_data

