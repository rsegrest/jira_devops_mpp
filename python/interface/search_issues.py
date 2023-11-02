import json
from interface.parse_json import get_issue_key, get_issue_type, get_summary, get_status
from interface.connect import connect_to_jira

def format_list(epic_keys):
    str = ''
    for epic_key in epic_keys:
        str += epic_key + ','
    return str[:-1]

def get_linked_issues_for_epiclist(
    issuetype=None,
    status=None
):
    """From Jira API, get issues -- may also be filtered by a given issuetype or status.
       No filter if 'ALL' given for issuetype or status

    Args:
        issuetype (string): Issue Type
        status (string): Status

    Returns:
        list of objects: Issues of type 'issuetype' and status 'status' (or 'ALL')
    """
    # start = time.time()

    # http://127.0.0.1:8080/rest/api/2/search?jql=project=MPPSAM&issuetype=story
    jira = connect_to_jira()
    jql_request = "project=MPPSAM"
    if (issuetype != None) and (issuetype != "ALL"):
        jql_request += '&issuetype=' + issuetype

    linked_issues = jira.jql(jql_request)
    
    return linked_issues

def handle_epic_list(issuetype, status=None):
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
    response = get_linked_issues_for_epiclist(issuetype, status)
    # if response is None:
    #     return []
    # if len(response) == 0:
    #     return []
    
    issue_list = response["issues"]
    num_issues = len(issue_list)
    print(f"{str(num_issues)} total issues returned for this search (in handle epic list)")
    # end = time.time()
    # if PERFORMANCE_ANALYSIS:
    #     print("handle_epic_list() took " + str(end - start) + " seconds")
    return issue_list

def extract_fields_from_json(issue_json):
    """Strips Issue JSON objects of data irrelevant to this app.

    Args:
        issue_json: issue object from Jira API
        epic_key: epic associated with this issue 

    Returns:
        list: type, key, summary, epic_link, status, and sprint link
              pulled from this issue's original metadata object 
    """
    # start = time.time()
    issue_type = get_issue_type(issue_json)
    issue_key = get_issue_key(issue_json)
    # summary = get_summary(issue_json)
    # epic_link = epic_key
    # current_status = get_status(issue_json)
    # sprint_link = get_sprint_link(issue_json)
    # end = time.time()
    # if PERFORMANCE_ANALYSIS:
        # print("get_sprints() took " + str(end - start) + " seconds")
    return [
        issue_type, issue_key,
        # summary, epic_link, current_status, sprint_link
    ]


def get_arrays_from_search(issuetype, status=None):
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
    print('checkpoint 1')
    # print(results)
    array_2d = []
    print(type(results))
    if len(results) == 0:
        return []
    print('checkpoint 2')
    # TODO: Loop and extract important fields from each issue
    # print(str(results[0]['fields']))
    # print(str(results[0]['fields']['issuetype']['name']))
    for issue in results:
        print('looping...')
        # print(str(issue['fields']))
        print(str(issue['fields']['issuetype']['name']))
        # next_field = extract_fields_from_json(issue)
        # array_2d.append(next_field)
    # for count, result in enumerate(results, 0):
    #     if len(result) == 0:
    #         print('No issues found.')
        # else:

    #         pass
            # result: class 'dict'
            # result.items(): class 'dict_items'
            # items = result.items()
            # print(len(result))
            # print(type(items))
            # print(type(result))
            # print(result.items())
            # result_json = json.loads(json.dumps(result))
            # for k,v in result.items():
            #     print('k,v:')
            #     print(k)
            #     print(v['issuetype']['id'])
                # print(k + ' : ' + v)
                # print(issue['id'])
                # json.loads(str(issue))
                # json_issue = json.loads(issue)
                # print(json_issue)
                # next_field = extract_fields_from_json(issue)
                # array_2d.append(next_field)
    # print(array_2d)
    return array_2d
    