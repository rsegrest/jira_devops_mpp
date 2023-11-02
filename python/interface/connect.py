from atlassian import Jira
import config
cfg = config.Config('jira.cfg')



def connect_with_username_and_password():
    jira = Jira(
        url='http://host.docker.internal:8080',
        username='rick',
        password='JIRApassword!123')
    return jira

# For server version only, Cloud edition doens't have PAT
def connect_with_personal_access_token():
    # [jiraURL]/secure/ViewProfile.jspa?selectedTab=com.atlassian.pats.pats-plugin:jira-user-personal-access-tokens
    
    jira_access_token = "NTE4MDc5MzU0Njk4OuypuPOv8L/8M+1gsWCNmvr6b2Ap"
    jira = Jira(
        url='http://host.docker.internal:8080',
        token=jira_access_token
    )
    return jira

def connect_with_api_key():
    # Create a token using this link (then log-in with your Atlassian Account)
    # https://id.atlassian.com/manage-profile/security/api-tokens
    jira_username = 'rick'
    jira_api_key = "ATATT3xFfGF0Wm3zg0GiKRJLUl7qpfHgCvTG0Y-ktD6o2ZCmCrp71BlIn0lSPonmkFFB3L8veiUi1qP_Ok1Kcv_bKK_5mJHHWDvghZTuTvv-xyS09qu1vINn8ZWnqCe1jnwyXH7QQNzwQXCBztQvGSTGyw5-_agkcpM-S2yucHMEwapqTdWgeog=CD2375BE"
    jira = Jira(
        url='http://host.docker.internal:8080',
        username=jira_username,
        password=jira_api_key,
        cloud=False
    )
    return jira

def step_one():

    # Try a query directly in the Browser:
    # Go to:
    # http://localhost:8080
    # Log-in
    # Try the following API URL:
    # http://localhost:8080/rest/api/2/project
    

    # Step 1 -- Connect:
    # jira = connect_with_username_and_password()
    # jira = connect_with_personal_access_token()
    jira = connect_with_api_key()
    # projects = jira.get_all_projects()
    # print(projects)

def step_two():

    # Step 2 -- Print out projects
    jira = connect_with_personal_access_token()
    projects = jira.get_all_projects()

    def output_id_name(proj):
        return [ proj['id'], proj['name'] ]

    proj_info = map(output_id_name, projects)

    for p in proj_info:
        print(p)

    projects = jira.get_all_projects()

# step_two()

def connect_to_jira():
    jira = connect_with_personal_access_token()
    return jira


# output to a site
# export to Excel / CSV

