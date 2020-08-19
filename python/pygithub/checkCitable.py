#!/usr/bin/python
from github import Github
from github import GithubException
import sys

def isPathInRepository(repo,path):
    try:
        repo.get_contents(path)
        print(f"Found {path} in repository")
        return True
    except GithubException:
        print(f"{path} not found in repository")
        return False  

g = Github()
# In case an access token is needed
#g = Github("access_token")
repo = g.get_repo(sys.argv[1])

assert(isPathInRepository(repo,"CITATION.json") or isPathInRepository(repo,"codemeta.json"))


