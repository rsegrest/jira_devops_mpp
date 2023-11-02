""" Methods to handle the complex metadata objects returned by Jira API """

def get_issue_type(issue):
    """Strips issue type (string) from an issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: name of issue type
    """
    print(issue)
    return issue["fields"]["issuetype"]["name"]


def get_issue_key(issue):
    """Strips issue key (string) from an issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: issue key
    """
    return issue["key"]


def get_fix_versions(issue):
    """Pulls a list of fix versions from a given issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        list of strings: names of fix versions associated with this issue
    """
    output_string = ""
    for fix_ver in issue["fields"]["fixVersions"]:
        output_string += fix_ver["name"]
    return output_string

def calc_pct_accurate(estimate, actual):
    """Calculates how accurate a work estimate is, vs.
       actual time recorded

    Args:
        estimate (number): estimate in seconds
        actual (number): actual time worked in seconds

    Returns:
        string: ratio of actual/estimate,
                formatted as string with two decimals
    """
    if estimate == 0:
        return 0
    if isinstance(estimate, str):
        try:
            estimate = float(estimate)
        except ValueError:
            return "--"
    if isinstance(actual, str):
        try:
            actual = float(actual)
        except ValueError:
            return "--"
    # return '{0:.2f}'.format((actual/estimate)*100)
    return f"{((actual/estimate)*100):.2f}"

def get_summary(issue):
    """Strips summary from issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: summary for given issue
    """
    return issue["fields"]["summary"]

def get_parent_epic(issue):
    """Gets parent epic from issue (epic) object, or
       "-" if not present in metadata

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: epic link, or "-" if epic link not available
    """
    if "customfield_10005" in issue["fields"]:
        return issue["fields"]["customfield_10005"]
    return "-"

def get_epic_link(issue):
    """Strips epic link from issue (epic) object, or
       "-" if not present in metadata

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: epic link, or "-" if epic link not available
    """
    if "customfield_10007" in issue["fields"]:
        return issue["fields"]["customfield_10007"]
    return "-"


def get_status(issue):
    """Strips status from issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: status name for given issue
    """
    status = issue["fields"]["status"]["name"]
    return status


def get_sprint_link(issue):
    """Strips sprint link from issue object

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string: sprint link for given issue
    """
    if issue["fields"]["customfield_10004"]:
        customfield = issue["fields"]["customfield_10004"]
        customfield_split = customfield[0].split(",")[3]
        sprint_name_field = customfield_split.split("=")[1]

        return sprint_name_field
    return "-"


def get_status_len(json_obj):
    """Finds statuses in issue JSON object, and returns length of embedded list

    Args:
        json_obj (object): JSON to parse 

    Returns:
        number: # of statuses in status list, embedded in JSON data
    """
    obj_arr_len = len(json_obj[0]["statuses"])
    return obj_arr_len


def build_issues_object(issues_json):
    """Create a simplified object that returns only type, key, summary, and
       status of an issue from its JSON object
    Args:
        issues_json (object): JSON to parse 

    Returns:
        object: simplified object with keys:
                issue_type, issue_key, summary, status
    """
    filtered_issues_array = []
    json_arr_len = len(issues_json["issues"])

    for i in range(0, json_arr_len):
        next_issue = issues_json["issues"][i]
        if next_issue not in filtered_issues_array:
            filtered_issues_array.append(
                {
                    "issue_type": get_issue_type(next_issue),
                    "issue_key": get_issue_key(next_issue),
                    "summary": get_summary(next_issue),
                    "status": get_status(next_issue),
                }
            )

    return filtered_issues_array


def get_version_name(version_json):
    """Finds version name in version JSON object

    Args:
        version_json (object): JSON to parse 

    Returns:
        string: version name from JSON object
    """
    return version_json["name"]


def get_statuses_json_for_issuetype(issue_type, all_statuses):
    """Gets statuses associated with an issuetype

    Args:
        issue_type (string): issue type
        all_statuses (list of objects): object with embedded status info

    Returns:
        list of strings: statuses found in object, or []
    """
    for status in all_statuses:
        if status["name"] == issue_type:
            return status["statuses"]
    return []


def get_status_name(status_json):
    """Finds statuses in issue JSON object, and returns length of embedded list

    Args:
        json_obj (object): JSON to parse 

    Returns:
        number: # of statuses in status list, embedded in JSON data
    """
    return status_json["name"]
