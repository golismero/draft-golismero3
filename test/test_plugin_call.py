from golismero3.plugin import plugin_runner
import json

def test_call_plugin():
    raw_inp = [
        {"_id": 1, "_type": "IP", "ip": "192.168.1.1"}
    ]
    inp = json.dumps(raw_inp)
    plugin = plugin_runner("cat examples/tool_output.json")
    res = list( plugin(inp) )
    
    expected_output = [
        [
            {"_id": 1, "_type": "IP", "ip": "192.168.1.1"},
            {"_id": "123", "_type": "PORT", "_tool": "cat examples/tool_output.json", "port": 80}
        ],
        [
            {"_id": 1, "_type": "IP", "ip": "192.168.1.1"},
            {"_id": "321", "_type": "PORT", "_tool": "cat examples/tool_output.json", "port": 81}
        ]
    ]
    
    assert res == expected_output

