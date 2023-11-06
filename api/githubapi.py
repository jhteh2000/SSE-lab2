import requests


class GitHubUser:
    def __init__(self, username):
        self.username = username
        self.response = requests.get(
            "https://api.github.com/users/" + username + "/repos"
        )

    def getRepoName(self):
        if self.response.status_code == 200:
            repos = self.response.json()
            # data returned is a list of ‘repository’ entities
            repo_name = []
            for repo in repos:
                repo_name.append(repo["full_name"])
        return repo_name

    def getRepoLastPushed(self):
        if self.response.status_code == 200:
            repos = self.response.json()
            # data returned is a list of ‘repository’ entities
            repo_last_updated = []
            for repo in repos:
                repo_last_updated.append(repo["pushed_at"])
        return repo_last_updated

    def getRepoLists(self):
        list_name = self.getRepoName()
        list_pushes = self.getRepoLastPushed()
        repo_list = zip(list_name, list_pushes)
        return repo_list
