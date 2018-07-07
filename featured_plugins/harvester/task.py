#!/usr/local/bin/python2
# -*- coding: utf-8 -*-

"""
Integration with `theHarvester <https://github.com/laramies/theHarvester>`_.
"""

import email_validator
import mmh3
import os, os.path
import socket
import StringIO
import sys
import traceback
import warnings

from email_validator import validate_email, EmailNotValidError

try:
    import cjson as json
except ImportError:
    try:
        import anyjson as json
    except ImportError:
        import json as json

# Add the current directory to the search path.
cwd = os.path.split(__file__)[0]
cwd = os.path.abspath(cwd)
sys.path.insert(0, cwd)
del cwd

# Preserve the real stdout.
stdout = sys.stdout

# Redirect stdout to stderr to send theHarvester output to the logs.
sys.stdout = sys.stderr

# Import the wrapper for theHarvester.
import theharvester_wrapper

# Helper function to validate hostnames.
def validate_hostname(hostname):
    try:
        socket.getaddrinfo(hostname, None, socket.AF_INET)
    except Exception:
        try:
            socket.getaddrinfo(hostname, None, socket.AF_INET6)
        except Exception:
            return False
    return True

# This is the tool name we will use for the output.
TOOL = "theHarvester 2.7"

# Get the hostname to be used as a search keyword.
word = json.load(sys.stdin)[0]["hostname"]

# This is where we'll put all of our output.
output = []

# This is where we collect all the emails and hosts we found.
emails, hostnames = set(), set()

# We will collect all errors here.
errors = []

# Search the hostname in each supported engine.
for search in theharvester_wrapper.ENGINES:
    print "Searching on: %s" % search.__doc__
    try:
        results = search(word)
    except Exception:
        errors.append(traceback.format_exc())
        continue
    errors.extend(results.get("errors", []))
    emails.update(results.get("emails", []))
    hostnames.update(results.get("hostnames", []))

# Convert the emails to the Golismero data model.
for email in sorted(emails):
    try:
        validate_email(email)
    except EmailNotValidError:
        errors.append(traceback.format_exc())
        continue
    output.append(
        {
            "_id": mmh3.hash128(email),
            "_type": "email",
            "_tool": TOOL,
            "email": email,
        }
    )

# Convert the hostnames to the Golismero data model.
for hostname in sorted(hostnames):
    if validate_hostname(hostname):
        output.append(
            {
                "_id": mmh3.hash128(hostname),
                "_type": "hostname",
                "_tool": TOOL,
                "hostname": hostname,
            }
        )

# Convert the errors to the Golismero data model.
for error in errors:
    output.append(
        {
            "_id": mmh3.hash128(error),
            "_type": "error",
            "_tool": TOOL,
            "error": error,
        }
    )

# Spit out all the output in JSON format to the real stdout.
json.dump([output], stdout)