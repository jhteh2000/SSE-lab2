import requests

response = requests.get("https://api.github.com/users/gene0524/repos")


def getRepoName():
    if response.status_code == 200:
        repos = response.json()
        # data returned is a list of ‘repository’ entities
        repo_name = []
        for repo in repos:
            repo_name.append(repo["full_name"])
    return repo_name


def getRepoLastPushed():
    if response.status_code == 200:
        repos = response.json()
        # data returned is a list of ‘repository’ entities
        repo_last_updated = []
        for repo in repos:
            repo_last_updated.append(repo["pushed_at"])
    return repo_last_updated


def getRepoLists():
    list_name = getRepoName()
    list_pushes = getRepoLastPushed()
    repo_list = zip(list_name, list_pushes)
    return repo_list
