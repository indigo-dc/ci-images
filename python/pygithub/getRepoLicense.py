#!/usr/bin/python
from github import Github
import sys

g = Github()
# In case an access token is needed
#g = Github("access_token")

repo = g.get_repo(sys.argv[1])
license = repo.get_license()
print("Found license for repository %s: %s" %(repo.name,license.license))
