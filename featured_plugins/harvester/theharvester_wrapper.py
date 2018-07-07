#!/usr/local/bin/python2
# -*- coding: utf-8 -*-
 
"""
Wrapper for theHarvester.
"""

import traceback

# Add the theHarvester directory to the search path.
import os
import sys
cwd = os.path.split(__file__)[0]
cwd = os.path.abspath(cwd)
cwd = os.path.join(cwd, "theHarvester")
sys.path.insert(0, cwd)
del cwd

import discovery
from discovery import *

LIMIT = 100
START = 0

def search_baidu(word):
    "Baidu"
    results = {}
    search = discovery.baidusearch.search_baidu(word=word, limit=LIMIT)
    search.process()
    try:
        results["emails"] = search.get_emails()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_bing(word):
    "Bing"
    results = {}
    search = discovery.bingsearch.search_bing(word=word, limit=LIMIT, start=START)
    search.process(api = "no")
    try:
        results["emails"] = search.get_emails()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_crtsh(word):
    "CRT.sh"
    results = {}
    search = discovery.crtsh.search_crtsh(word=word)
    search.process()
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_dogpile(word):
    "Dogpile"
    results = {}
    search = discovery.dogpilesearch.search_dogpile(word=word, limit=LIMIT)
    search.process()
    try:
        results["emails"] = search.get_emails()
    except Exception:
        error()
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_exalead(word):
    "Exaled"
    results = {}
    search = discovery.exaleadsearch.search_exalead(word=word, limit=LIMIT, start=START)
    search.process()
    try:
        results["emails"] = search.get_emails()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["files"] = search.get_files()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_googleplus(word):
    "Google+"
    results = {}
    search = discovery.googleplussearch.search_googleplus(word=word, limit=LIMIT)
    search.process()
    try:
        results["people"] = search.get_people()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_google(word):
    "Google Search"
    results = {}
    search = discovery.googlesearch.search_google(word=word, limit=LIMIT, start=START)
    search.process()
    try:
        results["emails"] = search.get_emails()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_jigsaw(word):
    "Jigsaw"
    results = {}
    search = discovery.jigsaw.search_jigsaw(word=word, limit=LIMIT)
    search.process()
    try:
        results["people"] = search.get_people()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_linkedin(word):
    "LinkedIn"
    results = {}
    search = discovery.linkedinsearch.search_linkedin(word=word, limit=LIMIT)
    search.process()
    try:
        results["people"] = search.get_people()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_netcraft(word):
    "Netcraft"
    results = {}
    search = discovery.netcraft.search_netcraft(word=word)
    search.process()
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_pgp(word):
    "PGP"
    results = {}
    search = discovery.pgpsearch.search_pgp(word=word)
    search.process()
    try:
        results["emails"] = search.get_emails()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_threatcrowd(word):
    "ThreatCrowd"
    results = {}
    search = discovery.threatcrowd.search_threatcrowd(word=word)
    search.process()
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_twitter(word):
    "Twitter"
    results = {}
    search = discovery.twittersearch.search_twitter(word=word, limit=LIMIT)
    search.process()
    try:
        results["people"] = search.get_people()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_virustotal(word):
    "VirusTotal"
    results = {}
    search = discovery.virustotal.search_virustotal(word=word)
    search.process()
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

def search_yahoo(word):
    "Yahoo"
    results = {}
    search = discovery.yahoosearch.search_yahoo(word=word, limit=LIMIT)
    search.process()
    try:
        results["emails"] = search.get_emails()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        error()
    return results

def search_yandex(word):
    "Yandex"
    results = {}
    search = discovery.yandexsearch.search_yandex(word=word, limit=LIMIT, start=START)
    search.process()
    try:
        results["emails"] = search.get_emails()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["hostnames"] = search.get_hostnames()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    try:
        results["files"] = search.get_files()
    except Exception:
        results.get("errors", []).append(traceback.format_exc()) 
    return results

# Commented out the engines that generally give problems.
ENGINES = (
    search_baidu,
    search_bing,
    # search_crtsh,         # Not present in the stable release.
    search_dogpile,
    search_exalead,
    search_google,
    # search_googleplus,    # Only produces People results, not yet suported.
    # search_jigsaw,        # Only produces People results, not yet suported.
    # search_linkedin,      # Only produces People results, not yet suported.
    # search_netcraft,      # Not present in the stable release.
    # search_pgp,           # Always times out when trying to connect to the server.
    # search_threatcrowd,   # Not present in the stable release.
    # search_twitter,       # Only produces People results, not yet suported.
    # search_virustotal,    # Not present in the stable release.
    search_yahoo,
    search_yandex,
)
