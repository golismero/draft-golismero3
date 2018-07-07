from golismero3.plugin import plugin_runner
import json
from pprint import pprint

def test_call_plugin():
    raw_inp = [
        {"_id": 1, "_type": "ip", "ip": "192.168.1.1"}
    ]
    inp = json.dumps(raw_inp)
    plugin = plugin_runner("cat examples/tool_output.json")
    res = list( plugin(inp) )
    
    expected_output = [
        [
            {"_id": 1, "_type": "ip", "ip": "192.168.1.1"},
            {"_id": "123", "_type": "port", "_cmd": "cat examples/tool_output.json", "port": 80}
        ],
        [
            {"_id": 1, "_type": "ip", "ip": "192.168.1.1"},
            {"_id": "321", "_type": "port", "_cmd": "cat examples/tool_output.json", "port": 81}
        ]
    ]

    print("res")
    pprint(res)
    print("exp")
    pprint(expected_output)
    
    assert res == expected_output

def test_fail_plugin():
    raw_inp = [
        {"_id": 1, "_type": "ip", "ip": "192.168.1.1"}
    ]
    inp = json.dumps(raw_inp)
    plugin = plugin_runner("echo 'Error!' 1>&2; exit 64")
    res = list( plugin(inp) )
    
    expected_output = [
        [
            {"_id": 1, "_type": "ip", "ip": "192.168.1.1"},
            {'_id': 212281217781803245129106443529066261547, '_type': 'error', 
                '_cmd': "echo 'Error!' 1>&2; exit 64", 'error': 'Error!\n'}
        ]
    ]

    print("res")
    pprint(res)
    print("exp")
    pprint(expected_output)
    
    assert res == expected_output

def test_multiple_element_return():
    raw_inp = [
        {"_id": 1, "_type": "domain", "domain": "bad.local"}
    ]
    inp = json.dumps(raw_inp)
    plugin = plugin_runner("cat examples/tool_multiple_output.json")
    res = list( plugin(inp) )
    
    expected_output = [
        [
            {
                "_id": 1, "_type": "domain", "domain": "bad.local"
            },
            {
                "_id": 2, "_type": "ip", "ip": "127.0.0.1",
                "_cmd": "cat examples/tool_multiple_output.json"
            },
            {
                "_id": 212281217781803245129106443529066261547, "_type": "vulnerability",
                "_cmd": "cat examples/tool_multiple_output.json",
                "cve": "CVE-2014-9999999", "cwe": "CWE-245", "description": "we are doom!"
            }
        ]
    ]
    print("res")
    pprint(res)
    print("exp")
    pprint(expected_output)
    
    assert res == expected_output
