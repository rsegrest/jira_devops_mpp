#!/bin/bash

# cURL is a command-line script that gets data from a URL
# Type "man curl" at the command line to see how it works and what options you can add

# https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/
https://ricksegrest.atlassian.net/rest/api/2/issue
BASE_URL=https://ricksegrest.atlassian.net

# GET PROJECTS
# curl -D- -u rick:JIRApassword!123 \
#     -X GET -H "Content-Type: application/json" \
#     ${BASE_URL}/rest/api/2/project

# Query to search for all issues in the "MPPSAM" project
JQL_QUERY="project=\\u002a"
# GET all issues that match query
curl -D- -u rsegrest77@gmail.com:B3rk5h1r3!atlassian \
    -X GET -H "Content-Type: application/json" \
    ${BASE_URL}/rest/api/2/issue


