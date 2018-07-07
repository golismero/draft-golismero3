import subprocess
import json

def plugin_runner(cmd):
    def _parse_input(inp):
        if not inp:
            return None
        b = bytearray()
        b.extend(inp.encode())
        return b
    def _parse_json(out):
        return json.loads(out)
    def _runner(inp=None):
        input_data = _parse_json(inp)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, stdin=subprocess.PIPE)
        stdout, stderr = p.communicate(input=_parse_input(inp))
        for elm in _parse_json(stdout):
            out = input_data.copy()
            out.append(elm)
            yield out
    return _runner