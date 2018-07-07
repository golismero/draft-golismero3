# -------------------------------------------------------------------------
#
# This plugin runs when a data type 'domain' got
#
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# We assumes that the input data was checked for correct number of fields
# -------------------------------------------------------------------------
import sys
import mmh3
import json
import logging
import platform

from typing import List
from golismero_helpers import Golismero3Exception, calculate_hash
from golismero_helpers.os_helpers import launch_command

log = logging.getLogger("golismero3")


def run_plugin(data: dict) -> List[dict or None]:

    port = data['port']
    domain = data['domain']

    log.info(f"Starting DNS information gathering for domain "
             f"{domain}")

    output_result = "/tmp/result.json"
    if platform.system() == "Darwin":
        binary = 'testssl.sh'
    else:
        binary = 'testssl'

    command = f"{binary} --jsonfile-pretty={output_result} " \
              f"--severity MEDIUM --sneaky -U -S -p " \
              f"{domain}:{port}"

    execution_result = launch_command(command,
                                      callback=(print, log.info),
                                      file_result=output_result)
    # -------------------------------------------------------------------------
    # Finding results
    # -------------------------------------------------------------------------
    json_execution_result = json.loads(execution_result)

    results = []
    for host in json_execution_result['scanResult']:

        # ---------------------------------------------------------------------
        # Recover vulnerabilities
        # ---------------------------------------------------------------------
        for vulnerability in host['vulnerabilities']:

            # -----------------------------------------------------------------
            # Build IP data
            # -----------------------------------------------------------------
            ip = {
                '_type': 'ip',
                'ip': host['ip']
            }
            ip['_id'] = calculate_hash(ip)

            # -----------------------------------------------------------------
            # Build vulnerability data
            # -----------------------------------------------------------------
            v = {
                '_type': 'vulnerability',
                'cve': vulnerability.get('cve', ""),
                'title': vulnerability['id'],
                'description': vulnerability.get('finding', ""),
                'cwe': vulnerability.get('cwe', "")
            }
            v['_id'] = mmh3.hash128(f"{ip['_id']}#{calculate_hash(v)}")

            results.append([ip, v])

    return results


def main() -> str:
    # -------------------------------------------------------------------------
    # Read input parameters via std-in
    # -------------------------------------------------------------------------
    with open(sys.stdin, "r") as f:
        input_data = f.read()

    # Text -> json
    input_as_json = json.loads(input_data)

    result = run_plugin(input_as_json)

    # Dump result to std-out
    return json.dumps(result)


if __name__ == '__main__':
    print(main())
