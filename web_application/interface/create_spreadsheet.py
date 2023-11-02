""" Methods to create spreadsheet for export using pandas """

import pandas as pd
from datetime import datetime
from io import BytesIO

def get_date_as_str():
    """Formats a date as string for use in filename

    Returns:
        string: date as string (YYYY_MM_DDThh-mm-ss)
    """
    return datetime.now().strftime("%Y_%m_%dT%H-%M-%S")
    
# TODO: remove?
def create_epic_filename():
    """Adds prefix to filename for epic report

    Returns:
        string: Filename with prefix and timestamp
    """
    return create_filename("epic_rpt_")

# TODO: remove?
def create_sprint_filename():
    """Adds prefix to filename for sprint report

    Returns:
        string: Filename with prefix and timestamp
    """
    return create_filename("sprint_")

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

def check_epic_row(text):
    """Check if row is an epic header

    Args:
        row (pandas dataframe row): Row to be checked

    Returns:
        boolean: True if row is an epic, False otherwise
    """
    if text.find('EPIC:') != -1:
        return True
    return False

def check_no_issues_row(text):
    """Check if row is a no issues header

    Args:
        row (pandas dataframe row): Row to be checked
        
    Returns:
        boolean: True if row is a no issues header, False otherwise
    """
    if text.find('No issues') != -1:
        return True
    return False

def create_ss_w_pandas(data, reporttype):
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

    epic_format = workbook.add_format({'bold': True, 'bg_color': '#FF8888'})
    no_issues_format = workbook.add_format({'bold': True, 'bg_color': '#FFBB88'})
    heading_format = workbook.add_format({'bold': True, 'font_size': 12, 'bg_color': '#FFBBBB', 'border': 1})

    formatindex = 0
    headingindex = 0
    if (reporttype == 'epicreport'):
        formatindex = 0
        headingindex = 1
        worksheet.set_row(headingindex, None, heading_format)
    elif (reporttype == 'sprintreport'):
        formatindex = 1
        
        
    for index, row in df1.iterrows():
        if index > formatindex:
            if check_no_issues_row(row[0]):
                worksheet.set_row(index+1, None, no_issues_format)
            elif check_epic_row(row[0]):
                worksheet.set_row(index+1, None, epic_format)
    
    writer.close()
    output.seek(0)
    return output

