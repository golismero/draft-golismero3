# -------------------------------------------------------------------------
#
# This plugin runs when a data type 'domain' got
#
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# We assumes that the input data was checked for correct number of fields
# -------------------------------------------------------------------------

from typing import List, Tuple

import mmh3
import logging
import dns.resolver

log = logging.getLogger("golismero3")


class Golismero3Exception(Exception):
    pass


DUMMY_DATA: list = [
    {
        '_id': mmh3.hash128("helloWorld"),
        '_type': 'domain',
        'domain': 'sueldonetoautonomo.es'
    },
    {
        '_id': mmh3.hash128("helloWorld"),
        '_type': 'ip',
        'ip': '165.227.229.13'
    }
]

DNS_TYPES = ('A', 'AAAA', 'NS', 'MX')
REGISTER_EXTRACTOR = {
    'A': lambda x: x.address,
    'AAAA': lambda x: x.address,
    'NS': lambda x: str(x.target),
    'MX': lambda x: str(x.exchange)
}


def parse_input_data(data: List[dict]) -> Tuple[dict, dict]:
    # First element must be a domain type
    if len(data) < 2:
        raise Golismero3Exception("Input data must have at least 2 "
                                  "linked data")

    domain = data[0]
    ip = data[1]

    if domain['_type'] != 'domain':
        raise Golismero3Exception("Type must be 'domain'")
    if ip['_type'] != 'ip':
        raise Golismero3Exception("Type must be 'ip'")

    return ip, domain


def run_plugin(data: List[dict]) -> List[dict]:

    ip, domain = parse_input_data(data)

    log.info(f"Starting DNS information gathering for domain "
             f"{domain['domain']}")

    results = []

    for dns_type in DNS_TYPES:
        try:
            response = dns.resolver.query(domain['domain'], dns_type)
        except Exception:
            continue

        # get returned value from query.
        for ans in response.response.answer:
            ips = [REGISTER_EXTRACTOR[dns_type](x) for x in ans.items]

            results.extend([{
                '_id': mmh3.hash128(f"{dns_type}{ip}"),
                '_type': dns_type,
                'value': ip
            } for ip in ips])

    return results


if __name__ == '__main__':
    result = run_plugin(DUMMY_DATA)

    print(result)
