#!/bin/bash

# cURL is a command-line script that gets data from a URL
# Type "man curl" at the command line to see how it works and what options you can add

# https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/

BASE_URL=http://host.docker.internal:8080

# GET PROJECTS
# curl -D- -u rick:JIRApassword!123 \
#     -X GET -H "Content-Type: application/json" \
#     ${BASE_URL}/rest/api/2/project

# Query to search for all issues in the "MPPSAM" project
JQL_QUERY="project=MPPSAM"
# GET all issues that match query
curl -D- -u rick:JIRApassword!123 \
    -X GET -H "Content-Type: application/json" \
    ${BASE_URL}/rest/api/2/search?jql=${JQL_QUERY}

