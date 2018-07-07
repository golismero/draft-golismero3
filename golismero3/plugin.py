import subprocess
import json
import mmh3

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
        input_data = [_parse_json(inp)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, stdin=subprocess.PIPE)
        stdout, stderr = p.communicate(input=_parse_input(inp))
        if stderr:
            out = input_data.copy()
            out.append({
                "_id": mmh3.hash128(stderr),
                "_type": "error",
                "_cmd": cmd,
                "error": stderr.decode()
            })
            yield out
        # for know data types use our own hash
        if stdout:
            for elm in _parse_json(stdout):
                for x in elm:
                    x["_cmd"] = cmd
                out = input_data.copy()
                yield out + elm
    return _runner