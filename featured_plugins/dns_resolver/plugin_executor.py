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
import dns.resolver

from typing import List, Tuple

from golismero_helpers import calculate_hash


log = logging.getLogger("golismero3")


DNS_TYPES = ('A', 'AAAA', 'NS', 'MX')
REGISTER_EXTRACTOR = {
    'A': lambda x: x.address,
    'AAAA': lambda x: x.address,
    'NS': lambda x: str(x.target),
    'MX': lambda x: str(x.exchange)
}


def run_plugin(data: dict) -> List[List[dict]]:

    domain = data['domain']

    log.info(f"Starting DNS information gathering for domain "
             f"{domain}")

    results = []

    a_registers = []

    for dns_type in DNS_TYPES:
        try:
            response = dns.resolver.query(domain, dns_type)
        except Exception:
            continue

        # get returned value from query.
        for ans in response.response.answer:
            query_result = [REGISTER_EXTRACTOR[dns_type](x) for x in ans.items]

            if dns_type in ("A", "AAAA"):
                a_registers.extend(query_result)

            for ip in a_registers:
                v_ip = {
                    '_type': 'ip',
                    'ip': ip
                }
                v_ip['_id'] = calculate_hash(v_ip)

                for q in query_result:

                    reg = {
                        '_type': dns_type,
                        'value': q
                    }
                    reg['_id'] = calculate_hash([v_ip, reg])

                    results.append([v_ip, reg])

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
