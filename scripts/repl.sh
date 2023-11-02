python -m venv ~/atlassian-api

# Activate the virtual environment
source ~/atlassian-api/bin/activate

python

with open('./api_token.txt') as file:
    api_token = file.read().rstrip()

api_token


from atlassian import Jira
# api_token = ATATT3xFfGF0J52v1DrQZn0wp5RLBlTW6er6wIDXo2gH-JQGi1qRJtA_ZptXmQBlIdMKxSTmowv18rZKqi1QSresSo3zwv35O3fBPdj7NbkCQ6uzoXip6vUhDMzPMhZLz_1vosys2Eravrtf05e9qRPs-zpvZgH5Y3n4lns_DKnhovVz-zZZa44=8ECC0E23

# def connect_with_username_and_password():
#     jira = Jira(
#         url='http://host.docker.internal:8080',
#         username='rick',
#         password='JIRApassword!123')
#     return jira

jira = Jira(
    url='https://ricksegrest.atlassian.net',
    token=api_token
)
jira

