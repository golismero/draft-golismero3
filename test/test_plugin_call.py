from golismero.plugin import plugin_runner
import json

def test_call_plugin():
    raw_inp = [
        {"_id": 1, "_type": "IP", "ip": "192.168.1.1"}
    ]
    inp = json.dumps(raw_inp)
    plugin = plugin_runner("cat examples/tool_output.json")
    res = list( plugin(inp) )
    print(res)

    expected_output = [
        [
            {"_id": 1, "_type": "IP", "ip": "192.168.1.1"},
            {"_id": "123", "_type": "PORT", "port": 80}
        ],
        [
            {"_id": 1, "_type": "IP", "ip": "192.168.1.1"},
            {"_id": "321", "_type": "PORT", "port": 81}
        ]
    ]
    results = list()
    assert res == expected_output

