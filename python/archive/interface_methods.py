""" Methods to connect to and interface with Jira API """
import json
from interface.connect import connect_to_jira
from interface.parse_json import (
    get_issue_key,
    get_issue_type,
    get_sprint_link,
    get_summary,
    get_status,
)
from auth.read_token import read_token
from output.write_results_to_file import write_to_file
# Add CERT_FILE to use https (SSL) instead of http
# CERT_FILE = './static_data/bundle.pem'

token = read_token()

# def get_stories_json(project="MPPSAM"):
#     """Given a fix version, returns the associated epics from Jira API
#     Args:
#         fv (string): Fix Version
#     Returns:
#         object list: Epics associated with fix version
#     """
#     jira = connect_to_jira()
#     # jql_request = 'project = '+project+'" AND type=STORY"'
#     jql_request = "project = MPPSAM AND type=STORY"
#     issues = jira.jql(jql_request)
#     return issues


def get_stories_json(project="MPPSAM"):
    """Given a fix version, returns the associated epics from Jira API
    Args:
        fv (string): Fix Version
    Returns:
        object list: Epics associated with fix version
    """
    jira = connect_to_jira()
    # jql_request = 'project = '+project+'" AND type=STORY"'
    jql_request = "project = MPPSAM AND type=STORY"
    issues = jira.jql(jql_request)
    return issues

stories = get_stories_json()
write_to_file(json.dumps(stories), "stories.json")

def get_issues(
    issuetype,
    # status
):
    """From Jira API, get issues linked any of the epics in a list (epic_key).
       May also be filtered by a given issuetype or status.
       No filter if 'ALL' given for issuetype or status

    Args:
        epic_key (string): Epic Key
        issuetype (string): Issue Type
        status (string): Status

    Returns:
        list of objects: Issues linked to given epic (epic_key),
                         filtered by issuetype and status (if not 'ALL')
    """
    jira = connect_to_jira()
    # jql_request = "project = SLS AND 'Epic Link' IN ("+format_list(epic_key_list)+")"

    if issuetype != 'ALL':
        jql_request += " AND type = '"+issuetype+"'"
    # if status != 'ALL':
    #     jql_request += " AND status = '"+status+"'"
    linked_issues = jira.jql(jql_request)
    
    return linked_issues

# def filter_by_epic(issue_list, epic_key):
#     issues_for_epic = filter(lambda issue: issue['fields']['customfield_10005'] == epic_key, issue_list)
#     return list(issues_for_epic)


def get_project_list():
    """From Jira API, gets list of SLS software versions.

    Returns:
        list of objects: Each object contains data for each version
    """
    jira = connect_to_jira()
    projects = jira.projects()
    return projects

def extract_fields_from_json(issue_json):
    """Strips Issue JSON objects of data irrelevant to this app.

    Args:
        issue_json: issue object from Jira API
        epic_key: epic associated with this issue 

    Returns:
        list: type, key, summary, epic_link, status, and sprint link
              pulled from this issue's original metadata object 
    """
    issue_type = get_issue_type(issue_json)
    issue_key = get_issue_key(issue_json)
    summary = get_summary(issue_json)
    current_status = get_status(issue_json)
    return [
        issue_type,
        issue_key,
        summary,
        current_status,
        # sprint_link
    ]


def get_arrays_from_search(issuetype, status):
    """Creates a two-dimensional array that will map to output table for
       Epic Search results.

    Args:
        fix_version (string): Fix Version (related to SLS FSW)
        issuetype: 'ALL' or filter for issuetype
        status: 'ALL' or filter for status

    Returns:
        2D list of strings: Matrix that contains data
                            for results table display
    """
    results = handle_epic_list(
        issuetype=issuetype,
        # status=status
    )
    array_2d = []
    if len(results) == 0:
        return []
    for count, result in enumerate(results, 0):
        if len(result) == 0:
            print('No issues found.')
        else:
            print('else (get_arrays_from_search):')
            print(len(result))
            for issue in result:
                next_field = extract_fields_from_json(issue)
                array_2d.append(next_field)
    return array_2d

def handle_epic_list(issuetype):
    """Loops through list of epics to return related issues,
       optionally filtered by issuetype and/or status

    Args:
        epic_keys (list of strings): SLS FSW Jira epics
        issuetype (string): 'ALL' or applies filter by issuetype
        status (string): 'ALL' or applies filter by status

    Returns:
        list of objects: list of all issue objects related to
                         any epics in epic_keys list 
    """
    # start = time.time()
    values = []
    response = get_issues(issuetype)
    if response is None:
        return []
    if len(response) == 0:
        return []
    
    issue_list = response["issues"]
    num_issues = len(issue_list)
    print(f"{str(num_issues)} total issues returned for this search")
    # end = time.time()
    # if PERFORMANCE_ANALYSIS:
    #     print("handle_epic_list() took " + str(end - start) + " seconds")
    return values