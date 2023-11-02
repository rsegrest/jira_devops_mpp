""" Methods to connect to and interface with Jira API """
from interface.connect import connect_to_jira
from interface.parse_json import (
    get_issue_key,
    get_issue_type,
    get_sprint_link,
    get_summary,
    get_status,
)
from output.write_results_to_file import write_to_file
from auth.read_token import read_token
# Add CERT_FILE to use https (SSL) instead of http
# CERT_FILE = './static_data/bundle.pem'

token = read_token()

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
write_to_file(stories)

def get_linked_issues_for_epiclist(
    epic_key_list,
    issuetype,
    status
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
    if epic_key_list == None:
        return []
    if len(list(epic_key_list)) == 0:
        return []
    
    jira = connect_to_jira()
    # jql_request = "project = SLS AND 'Epic Link' IN ("+format_list(epic_key_list)+")"

    if issuetype != 'ALL':
        jql_request += " AND type = '"+issuetype+"'"
    if status != 'ALL':
        jql_request += " AND status = '"+status+"'"
    linked_issues = jira.jql(jql_request)
    
    return linked_issues

def filter_by_epic(issue_list, epic_key):
    issues_for_epic = filter(lambda issue: issue['fields']['customfield_10005'] == epic_key, issue_list)
    return list(issues_for_epic)    


def get_project_list():
    """From Jira API, gets list of SLS software versions.

    Returns:
        list of objects: Each object contains data for each version
    """
    jira = connect_to_jira()
    projects = jira.projects()
    return projects

# TODO: Fix to work with sample data
# def extract_fields_from_json():
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
    epic_link = epic_key
    current_status = get_status(issue_json)
    sprint_link = get_sprint_link(issue_json)
    return [
        issue_type, issue_key, summary, epic_link, current_status, sprint_link]


# def get_arrays_from_search(fix_version, issuetype, status):
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
    epic_list = get_list_of_epics(fix_version)
    epic_keys = epic_list['key_array']
    epic_statuses = epic_list['status_array']
    results = handle_epic_list(
        epic_keys=epic_keys,
        issuetype=issuetype,
        status=status
    )
    array_2d = []
    if len(results) == 0:
        return []
    for count, result in enumerate(results, 0):
        if len(result) == 0:
            array_2d.append(
                ['No issues associated with EPIC: '
                 + epic_keys[count] + ' meeting the current search criteria'])
        else:
            array_2d.append(
                ['EPIC: '+epic_keys[count]+', Status is: '+epic_statuses[count]])
            for issue in result:
                next_field = extract_fields_from_json(issue, epic_keys[count])
                array_2d.append(next_field)
    return array_2d
