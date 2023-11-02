import interface.connect as connect
# PyTest filenames begin with "test_*.py"
# example function
# def func(x):
#     return x + 1

# example test-- must begin with "test_"...
# This one fails. ( == 4 is passing )
# def test_answer():
#     assert func(3) == 5

def test_connect():
    jira_api_key = connect.connect_with_api_key()
    jira_pat = connect.connect_with_personal_access_token()
    jira_username_passwd = connect.connect_with_username_and_password()

    assert jira_api_key != None
    assert jira_pat != None
    assert jira_username_passwd != None

    