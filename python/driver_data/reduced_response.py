# issue_id: response.id
# issue_key: response.key
# issue_type: response.fields.issuetype.name
# timespent: response.fields.timespent
# project: response.fields.project.name
# priority: response.fields.priority.name
# assignee_name: response.fields.assignee.name
# status_name: response.fields.status.name

# created: response.fields.created
# resolution_date: response.fields.resolutiondate
# story_points: response.fields.customfield_10111 # Work done?

custom_fields = [
    {'id': 'customfield_10000', 'name': 'Development'},
    {'id': 'customfield_10106', 'name': 'Epic Colour'},
    {'id': 'customfield_10109', 'name': 'Epic Link'},
    {'id': 'customfield_10104', 'name': 'Epic Name'},
    {'id': 'customfield_10105', 'name': 'Epic Status'},
    {'id': 'customfield_10103', 'name': 'Original story points'},
    {'id': 'customfield_10100', 'name': 'Parent Link'},
    {'id': 'customfield_10108', 'name': 'Rank'},
    {'id': 'customfield_10110', 'name': 'Sprint'},
    {'id': 'customfield_10111', 'name': 'Story Points'},
    {'id': 'customfield_10102', 'name': 'Target end'},
    {'id': 'customfield_10101', 'name': 'Target start'},
    {'id': 'customfield_10107', 'name': 'Team'}
]
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
            'archivedby': None
    }
}
print(response['id'])