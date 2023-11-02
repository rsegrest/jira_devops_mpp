from output.string_format import reduce_decimal_string

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
            table_html += str(reduce_decimal_string(row[k]))
            table_html += '</td>'
        table_html += '</tr>'
    return table_html
