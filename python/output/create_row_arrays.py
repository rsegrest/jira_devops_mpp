from interface.simplify_object import simplify_object
from util.check_key import check_key

renamed_fields_for_row = ['issue_id', 'issue_key', 'issue_type', 'timespent', 'project', 'priority', 'assignee_name', 'status_name', 'created', 'resolution_date', 'story_points']


def convert_to_rows_array(obj_array):
    output_array = []
    for o in obj_array:
        if o == None:
            output_array.append(None)
        simple_object = simplify_object(o)
        output_array.append(convert_to_row_array(simple_object))
    return output_array

def convert_to_row_array(simple_object, renamed_fields=renamed_fields_for_row):
    row = []
    for field in renamed_fields:
        if check_key(simple_object, field):
            row.append(simple_object[field])
        else:
            row.append(None)
    return row

def get_custom_field_headings_array(object):
    objkeys = list(object.keys())
    headings = []
    for k in objkeys:
        k = k.replace("_"," ")
        k = k.title()
        k = k.replace(" Id"," ID")
        headings.append(k)
    return headings
