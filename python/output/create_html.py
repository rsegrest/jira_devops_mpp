from interface.simplify_object import simplify_object
from output.create_row_arrays import convert_to_row_array, convert_to_rows_array
from interface.search_issues import get_linked_issues_for_epiclist
import output.string_format as sf


def build_html_table(issuetype=None):
    headings_array = ['Issue ID','Issue Key','Issue Type','Time Spent','Project','Priority','Assignee Name','Status Name','Created','Resolution Date','Story Points']
    output_html_string = ''
    output_html_string = '<table><thead><tr>'
    for heading in headings_array:
        output_html_string += '<th>' + heading + '</th>'
    response = get_linked_issues_for_epiclist(issuetype)
    issues = response['issues']
    output_array = convert_to_rows_array(issues)
    if (len(output_array) == 0):
        output_html_string += '<tr><td colspan="11" class="no-issues-row">No issues found</td></tr>'
    else:
        output_html_string += convert_rows_array_to_html(output_array)
    output_html_string += '</tr></thead><tbody>'

    return output_html_string    
def convert_response_to_html_table(response):
    issues = response['issues']
    output_array = convert_to_rows_array(issues)
    return output_array

def get_headings_array():
    pass

def convert_rows_array_to_html(issues_row_array):
    output_html_string = ''
    output_html_string += '<tbody>'
    for row in issues_row_array:
        output_html_string += '<tr>'
        for value in row:
            output_html_string += '<td>' + str(value) + '</td>'
        output_html_string += '</tr>'
    output_html_string += '</tbody>'
    return output_html_string
    
# TODO: UNNEEDED?
def get_table_from_results(table_data):
    """Adds HTML to 2D array to create results table for SLS Epics &
       associated issues

    Args:
        table_data (2D array): data for table in 2D array format

    Returns:
        string (HTML): HTML to display table for epic-issue report
    """
    table_html = ""
    for row in table_data:
        table_html += "<tr class='results_row'>"
        for col in row:
            if (len(row)) == 1:
                table_html += "<td class='epic_heading' colspan='6'>"+col+"</td>"
                continue
            table_html += "<td class='results_cell'>"
            table_html += col
            table_html += '</td>'
        table_html += '</tr>'
    return table_html

# TODO: UNNEEDED?
def get_table_from_sprint_metrics(sprint_table_data):
    """Adds HTML to 2D array to create display table for Sprint report

    Args:
        sprint_table_data (2D array): data for table in 2D array format

    Returns:
        string (HTML): HTML to display table for sprint report
    """
    table_html = ""
    for row in sprint_table_data:
        column_keys = ["key", "summary", "fixVersions",
                       "status", "estimateInDays",
                       "remainingEstimateInDays",
                       "manDays", "pctAccurate"]
        table_html += "<tr class='results_row'>"
        for k in column_keys:
            table_html += "<td class='results_cell'>"
            table_html += str(sf.reduce_decimal_string(row[k]))
            table_html += '</td>'
        table_html += '</tr>'
    return table_html
