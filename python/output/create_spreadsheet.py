
import pandas as pd
from flask import send_file
from datetime import datetime
from io import BytesIO

from output.create_row_arrays import convert_to_rows_array
from interface.search_issues import get_linked_issues_for_epiclist

def create_spreadsheet(issuetype=None):
    results = get_linked_issues_for_epiclist(issuetype)
    issues = results['issues']
    results_array = convert_to_rows_array(issues)
    output = create_ss_w_pandas([
            # [], # headings
            *results_array],
        )
    return send_file(output, download_name=create_filename(), as_attachment=True)


def create_filename(prefix=None):
    """Generates filename based on timestamp, with .xlsx extension

    Returns:
        string: Filename
    """
    filename = get_date_as_str()+'.xlsx'
    if prefix is not None:
        return prefix+filename
    return filename

def get_col_widths(df):
    """Find maximum length of column data elements

    Args:
        dataframe (pandas dataframe): Data to be exported to spreadsheet

    Returns:
        int: maximum length of column data elements
    """
    idx_max = max([len(str(s)) for s in df.index.values] + [len(str(df.index.name))])
    return [idx_max] + [max([len(str(s)) for s in df[col].values] + [len(str(col))]) for col in df.columns]

def create_ss_w_pandas(data):
    """Create spreadsheet using pandas

    Args:
        data (pandas dataframe): Data to be exported to spreadsheet

    Returns:
        BytesIO object: File handle for spreadsheet
    """ 
    df1 = pd.DataFrame(data)
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df1.to_excel(writer, startrow = 0, merge_cells = False, sheet_name = "Sheet_1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["Sheet_1"]
    
    for i, width in enumerate(get_col_widths(df1)):
        worksheet.set_column((i-1), (i-1), width)

    issue_format = workbook.add_format({'bold': True, 'bg_color': '#FF8888'})
    heading_format = workbook.add_format({'bold': True, 'font_size': 12, 'bg_color': '#FFBBBB', 'border': 1})

    # formatindex = 0
    headingindex = 0
        # worksheet.set_row(headingindex, None, heading_format)
    # elif (reporttype == 'sprintreport'):
    formatindex = 1
        
    writer.close()
    output.seek(0)
    return output




def get_date_as_str():
    """Formats a date as string for use in filename

    Returns:
        string: date as string (YYYY_MM_DDThh-mm-ss)
    """
    return datetime.now().strftime("%Y_%m_%dT%H-%M-%S")