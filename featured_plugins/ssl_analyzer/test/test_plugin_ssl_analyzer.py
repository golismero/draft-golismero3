import json
import os.path as op

import featured_plugins.ssl_analyzer.plugin_executor

from ..plugin_executor import main

HERE = op.dirname(__file__)


def test_plugin_ssl_analyzer_successful(monkeypatch):

    def fake(command,callback, file_result):
        return open(op.join(HERE, "result.json"), "r").read()

    monkeypatch.setattr('sys.stdin', open(
        op.join(HERE, "input_example.json")))
    featured_plugins.ssl_analyzer.plugin_executor.launch_command = fake

    result = main()
    output_json = json.loads(result)

    for object_data in output_json:
        assert len(object_data) == 2
        assert object_data[0]['_type'] == 'ip'
        assert object_data[1]['_type'] == 'vulnerability'

