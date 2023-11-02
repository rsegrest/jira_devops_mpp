
from readconfig import read_config_file
from atlassian import Jira


class TestConfig:

    def test_get_issue_types_for_dropdown(self):
        issue_types = self.get_issue_types()
        assert issue_types != None
        assert len(issue_types) > 0
        # we only want the names of the issue types
        issue_names = []
        for issue in issue_types:
            issue_names.append(self.strip_issue_types(issue))
        # We want to get unique names only
        # casting the list to a set,
        # then back to a list will get rid of duplicates
        issue_names = self.get_issue_type_names_for_dropdown()
        # We will replace this:
        expected_list = ['ALL', 'Bug', 'Epic', 'Story', 'Subtask', 'Task']
        # expected_list = []
        assert issue_names == expected_list

    # def test_read_config_file(self):
    #     config = read_config_file()
    #     assert config != None

    #     # load each value into a variable
    #     username = config['username']
    #     url = config['url']
    #     token = config['token']

    #     assert username != None
    #     assert url != None
    #     assert token != None

    #     assert isinstance(username, str)
    #     assert isinstance(url, str)
    #     assert isinstance(token, str)

    def connect_with_token(self):
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

    def test_connect(self):
        jira = self.connect_with_token()
        assert jira != None

    def get_projects(self):
        jira = self.connect_with_token()
        projects = jira.get_all_projects()
        return projects

    def test_get_projects(self):
        projects = self.get_projects()
        assert len(projects) == 3
