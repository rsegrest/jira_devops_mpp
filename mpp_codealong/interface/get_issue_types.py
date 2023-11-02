from readconfig import read_config_file
from atlassian import Jira


def get_issue_types():
    issue_types = []
    jira = connect_with_token()
    issue_types = jira.get_issue_types()
    return issue_types


def connect_with_token():
    config = read_config_file()
    username = config['username']
    url = config['url']
    token = config['token']
    jira = Jira(
        url=url,
        username=username,
        password=token,
        cloud=True
    )
    return jira


def test_connect():
    jira = connect_with_token()
    assert jira != None


def get_projects():
    jira = connect_with_token()
    projects = jira.get_all_projects()
    return projects


def get_issue_type_names_for_dropdown():
    issue_types = get_issue_types()
    issue_names = []
    for issue in issue_types:
        issue_names.append(strip_issue_types(issue))
    # Want to get unique names only
    issue_names = [*set(issue_names)]
    issue_names.sort()
    # prepend ALL to the list
    return ['ALL', *issue_names]


def strip_issue_types(issue_type):
    return issue_type['name']
