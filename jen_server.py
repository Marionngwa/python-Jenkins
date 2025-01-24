import jenkins
import csv

jenkins_url = "http://3.238.44.78:8080"
username = "admin"
password = "devops"
server = jenkins.Jenkins(jenkins_url, username, password)


# print(server.get_whoami()["fullName"])
# print("***************")
# print(server.jobs_count())
_jobs = server.get_jobs()
all_jobs = []

for item in _jobs:
    print("")
    all_jobs.append([item.get('name'), item.get('url')])
print(all_jobs)


