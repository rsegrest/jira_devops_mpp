from interface.simplify_object import simplify_object, rename_custom_field
from interface.get_fields import get_custom_fields
from output.create_row_arrays import get_custom_field_headings_array, convert_to_row_array
response = {
    'id': '10022',
    'key': 'MPPSAM-23',
    'fields':
    {
        'issuetype':
        {
            'id': '10002',
            'name': 'Story',
            'subtask': False
        },
        'timespent': None,
        'project': {
            'id': '10000',
            'key': 'MPPSAM', 'name': 'mpp-sample', 'projectTypeKey': 'software',
        },
        'fixVersions': [{
            'id': '10000',
            'name': 'Version 1.0',
            'releaseDate': '2023-06-17'
        }],
        'customfield_10111': 2.0,
        'aggregatetimespent': None,
        'resolution': {
            'id': '10000',
            'name': 'Done'
        },
        'resolutiondate': '2023-06-15T14:54:25.000+0000',
        'workratio': -1,
        'lastViewed': '2023-07-02T15:12:17.760+0000',
        'created': '2023-06-03T06:19:25.000+0000',
        'priority': {
            'name': 'Medium',
            'id': '3'
        },
        'timeestimate': None,
        'aggregatetimeoriginalestimate': None,
        'versions': [], 'issuelinks': [],
        'assignee': {
            'self': 'http://host.docker.internal:8080/rest/api/2/user?username=rick',
            'name': 'rick', 'key': 'JIRAUSER10000', 'emailAddress': 'rsegrest77@gmail.com',
            'displayName': 'rsegrest77@gmail.com',
            'active': True,
            'timeZone': 'America/Chicago'
        },
        'updated': '2023-06-15T14:54:25.000+0000',
        'status': {
            'name': 'Done', 'id': '10001',
            'statusCategory': {
                'id': 3, 'key': 'done', 'colorName': 'success', 'name': 'Done'
            }
        },
        'timeoriginalestimate': None,
        'aggregatetimeestimate': None,
        'summary': "As a user, I'd like a historical story to show in reports",
        'creator': {
            'name': 'rick',
            'key': 'JIRAUSER10000',
            'emailAddress': 'rsegrest77@gmail.com',
            'displayName': 'rsegrest77@gmail.com',
            'active': True,
            'timeZone': 'America/Chicago'
        },
        'reporter': {
            'name': 'rick', 'key': 'JIRAUSER10000', 'emailAddress': 'rsegrest77@gmail.com',
            'displayName': 'rsegrest77@gmail.com',
            'active': True, 'timeZone': 'America/Chicago'
        },
        'aggregateprogress': {
            'progress': 0,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'total': 0}, 'environment': None, 'duedate': None, 'progress': {'progress': 0, 'total': 0},
            'comment': {
                'comments': [
                    {
                        'self': 'http://host.docker.internal:8080/rest/api/2/issue/10022/comment/10018',
                        'id': '10018',
                        'author': {
                            'name': 'rick',
                            'key': 'JIRAUSER10000',
                            'emailAddress': 'rsegrest77@gmail.com',
                            'displayName': 'rsegrest77@gmail.com',
                            'active': True, 'timeZone': 'America/Chicago'
                        },
                        'body': 'Joined Sample Sprint 1 21 days 10 hours 20 minutes ago\r\nTo Do to Done 9 days 1 hours 45 minutes ago',
                        'updateAuthor': {'self': 'http://host.docker.internal:8080/rest/api/2/user?username=rick', 'name': 'rick', 'key': 'JIRAUSER10000', 'emailAddress': 'rsegrest77@gmail.com', 'avatarUrls': {'48x48': 'http://host.docker.internal:8080/secure/useravatar?avatarId=10336', '24x24': 'http://host.docker.internal:8080/secure/useravatar?size=small&avatarId=10336', '16x16': 'http://host.docker.internal:8080/secure/useravatar?size=xsmall&avatarId=10336', '32x32': 'http://host.docker.internal:8080/secure/useravatar?size=medium&avatarId=10336'}, 'displayName': 'rsegrest77@gmail.com', 'active': True, 'timeZone': 'America/Chicago'}, 'created': '2023-06-15T14:54:25.088+0000', 'updated': '2023-06-15T14:54:25.088+0000'
                    }
                ],
        },
        'votes': {
            'self': 'http://host.docker.internal:8080/rest/api/2/issue/MPPSAM-23/votes',
            'votes': 0, 'hasVoted': False
        },
        'worklog': {'startAt': 0, 'maxResults': 20, 'total': 0, 'worklogs': []},
        'archivedby': None,
        'customfield_10000': '{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@337f5620[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@39fcfe05[overall=PullRequestOverallBean{stateCount=0, state=\'OPEN\', details=PullRequestOverallDetails{openCount=0, mergedCount=0, declinedCount=0}},byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@11031f1f[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@4f51c7ec[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@621b7ee3[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@1e80c19d[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1772ceb5[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@56dd1510[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@6f08954e[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@771c3d1b[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@761a422b[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@48d1bc6d[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={"cachedValue":{"errors":[],"configErrors":[],"summary":{"pullrequest":{"overall":{"count":0,"lastUpdated":null,"stateCount":0,"state":"OPEN","details":{"openCount":0,"mergedCount":0,"declinedCount":0,"total":0},"open":true},"byInstanceType":{}},"build":{"overall":{"count":0,"lastUpdated":null,"failedBuildCount":0,"successfulBuildCount":0,"unknownBuildCount":0},"byInstanceType":{}},"review":{"overall":{"count":0,"lastUpdated":null,"stateCount":0,"state":null,"dueDate":null,"overDue":false,"completed":false},"byInstanceType":{}},"deployment-environment":{"overall":{"count":0,"lastUpdated":null,"topEnvironments":[],"showProjects":false,"successfulCount":0},"byInstanceType":{}},"repository":{"overall":{"count":0,"lastUpdated":null},"byInstanceType":{}},"branch":{"overall":{"count":0,"lastUpdated":null},"byInstanceType":{}}}},"isStale":false}}'
    }
}
simple_object = {'issue_id': '10022', 'issue_key': 'MPPSAM-23', 'issue_type': 'Story', 'timespent': None, 'project': 'mpp-sample', 'priority': 'Medium', 'assignee_name': 'rick', 'status_name': 'Done', 'created': '2023-06-03T06:19:25.000+0000', 'resolution_date': '2023-06-15T14:54:25.000+0000', 'development': '{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@337f5620[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@39fcfe05[overall=PullRequestOverallBean{stateCount=0, state=\'OPEN\', details=PullRequestOverallDetails{openCount=0, mergedCount=0, declinedCount=0}},byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@11031f1f[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@4f51c7ec[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@621b7ee3[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@1e80c19d[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1772ceb5[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@56dd1510[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@6f08954e[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@771c3d1b[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@761a422b[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@48d1bc6d[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={"cachedValue":{"errors":[],"configErrors":[],"summary":{"pullrequest":{"overall":{"count":0,"lastUpdated":null,"stateCount":0,"state":"OPEN","details":{"openCount":0,"mergedCount":0,"declinedCount":0,"total":0},"open":true},"byInstanceType":{}},"build":{"overall":{"count":0,"lastUpdated":null,"failedBuildCount":0,"successfulBuildCount":0,"unknownBuildCount":0},"byInstanceType":{}},"review":{"overall":{"count":0,"lastUpdated":null,"stateCount":0,"state":null,"dueDate":null,"overDue":false,"completed":false},"byInstanceType":{}},"deployment-environment":{"overall":{"count":0,"lastUpdated":null,"topEnvironments":[],"showProjects":false,"successfulCount":0},"byInstanceType":{}},"repository":{"overall":{"count":0,"lastUpdated":null},"byInstanceType":{}},"branch":{"overall":{"count":0,"lastUpdated":null},"byInstanceType":{}}}},"isStale":false}}', 'story_points': 2.0}
custom_fields = [{'id': 'customfield_10000', 'name': 'Development'},{'id': 'customfield_10106', 'name': 'Epic Colour'},{'id': 'customfield_10109', 'name': 'Epic Link'},{'id': 'customfield_10104', 'name': 'Epic Name'},{'id': 'customfield_10105', 'name': 'Epic Status'},{'id': 'customfield_10103', 'name': 'Original story points'},{'id': 'customfield_10100', 'name': 'Parent Link'},{'id': 'customfield_10108', 'name': 'Rank'},{'id': 'customfield_10110', 'name': 'Sprint'},{'id': 'customfield_10111', 'name': 'Story Points'},{'id': 'customfield_10102', 'name': 'Target end'},{'id': 'customfield_10101', 'name': 'Target start'},{'id': 'customfield_10107', 'name': 'Team'}]
default_fields = ['Development','Epic Colour','Epic Link','Epic Name','Epic Status','Original story points','Parent Link','Rank','Sprint','Story Points','Target end','Target start','Team']
renamed_fields = ['development','epic_color','epic_link','epic_name','epic_status','original_story_points','parent_link','rank','sprint','story_points','target_end','target_start','team']
renamed_fields_for_row = ['issue_id', 'issue_key', 'issue_type', 'timespent', 'project', 'priority', 'assignee_name', 'status_name', 'created', 'resolution_date', 'story_points']

expected_headings_array = ['Issue ID','Issue Key','Issue Type','Timespent','Project','Priority','Assignee Name','Status Name','Created','Resolution Date','Development','Story Points']
expected_row = ['10022', 'MPPSAM-23', 'Story', None, 'mpp-sample', 'Medium', 'rick', 'Done', '2023-06-03T06:19:25.000+0000', '2023-06-15T14:54:25.000+0000', 2.0]

def test_get_headings_array():
    assert get_custom_field_headings_array(simple_object) == expected_headings_array

def test_get_headings_array():
    assert convert_to_row_array(simple_object, renamed_fields_for_row) == expected_row
