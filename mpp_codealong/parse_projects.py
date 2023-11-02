my_projects = [
    {
        "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
        "self": "https://ricksegrest.atlassian.net/rest/api/2/project/10000",
        "id": "10000",
        "key": "SP",
        "name": "scrum-project",
        "avatarUrls": {
            "48x48": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10407",
            "24x24": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10407?size=small",
            "16x16": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10407?size=xsmall",
            "32x32": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10407?size=medium",
        },
        "projectTypeKey": "software",
        "simplified": True,
        "style": "next-gen",
        "isPrivate": False,
        "properties": {},
        "entityId": "68f679b0-cd45-4e02-bdcd-bb7636223930",
        "uuid": "68f679b0-cd45-4e02-bdcd-bb7636223930",
    },
    {
        "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
        "self": "https://ricksegrest.atlassian.net/rest/api/2/project/10001",
        "id": "10001",
        "key": "SKB",
        "name": "Sample-Kanban-Board",
        "avatarUrls": {
            "48x48": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10425",
            "24x24": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10425?size=small",
            "16x16": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10425?size=xsmall",
            "32x32": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10425?size=medium",
        },
        "projectTypeKey": "software",
        "simplified": True,
        "style": "next-gen",
        "isPrivate": False,
        "properties": {},
        "entityId": "6fbb2adc-1e40-4adf-acc2-cc956304b2fe",
        "uuid": "6fbb2adc-1e40-4adf-acc2-cc956304b2fe",
    },
    {
        "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
        "self": "https://ricksegrest.atlassian.net/rest/api/2/project/10002",
        "id": "10002",
        "key": "DAAS",
        "name": "DaaS",
        "avatarUrls": {
            "48x48": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10419",
            "24x24": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10419?size=small",
            "16x16": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10419?size=xsmall",
            "32x32": "https://ricksegrest.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10419?size=medium",
        },
        "projectTypeKey": "software",
        "simplified": True,
        "style": "next-gen",
        "isPrivate": False,
        "properties": {},
        "entityId": "766eb93d-2f61-4244-b816-b8abcf2eb1ab",
        "uuid": "766eb93d-2f61-4244-b816-b8abcf2eb1ab",
    },
]
# 'id': '10000',
# 'key': 'SP',
# 'name': 'Sample-Kanban-Board',
if __name__ == "__main__":
    for p in my_projects:
        if "id" in p:
            print(p['id'])
        if "name" in p:
            print(p['name'])
        if "key" in p:
            print(p['key'])
        print('===============================================')
