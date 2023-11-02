from parse_json import get_status_len

def filter_unique_fixversions(fv_json):
    """Removes fix version duplicates from JSON object

    Args:
        fv_json (object): Fix Version JSON object

    Returns:
        string: list of fix versions with no duplicate entries
    """
    fv_array = []
    json_arr_len = len(fv_json)

    for i in range(0, json_arr_len):
        next_fixversion = fv_json[i]
        if next_fixversion not in fv_array:
            fv_array.append(fv_json[i]["name"])

    return fv_array


def filter_unique_statuses(st_json):
    """Removes status duplicates from JSON object

    Args:
        st_json (object): status JSON object

    Returns:
        string: list of statuses with no duplicate entries
    """
    status_array = []
    json_arr_len = get_status_len(st_json)

    for i in range(0, json_arr_len):
        next_status = st_json[0]["statuses"][i]["statusCategory"]["name"]
        if next_status not in status_array:
            status_array.append(st_json[0]["statuses"][i][
                "statusCategory"]["name"])

    return status_array


def filter_unique_epics(epic_json):
    """Removes epic duplicates from JSON object

    Args:
        epic_json (object): Epic JSON object

    Returns:
        string: list of epics with no duplicate entries
    """
    epics_array = []
    json_arr_len = len(epic_json["issues"])
    for i in range(0, json_arr_len):
        next_epic = epic_json["issues"][i]["key"]
        if next_epic not in epics_array:
            epics_array.append(next_epic)

    return epics_array
