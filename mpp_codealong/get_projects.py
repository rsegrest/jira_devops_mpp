from readconfig import read_config_file
from atlassian import Jira


def connect_with_token():
    config = read_config_file()
    username = config['username']
    url = config['url']
    token = config['token']
    jira = Jira(
        url=url,
        username=username,
        password=token,
        cloud=True
    )
    return jira


def get_projects():
    jira = connect_with_token()
    projects = jira.get_all_projects()
    return projects


if __name__ == "__main__":
    print(get_projects())
