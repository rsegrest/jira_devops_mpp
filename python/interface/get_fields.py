""" Methods to connect to and interface with Jira API """
from interface.connect import connect_to_jira
from auth.read_token import read_token

token = read_token()

def get_custom_fields():
    jira = connect_to_jira()
    fields = jira.get_custom_fields()
    values = fields['values']
    mapped_values = map(lambda x: {'id': x['id'], 'name': x['name']}, values)
    return list(mapped_values)
# get_custom_fields()