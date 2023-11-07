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

    def getRepoCreatedDate(self):
        if self.response.status_code == 200:
            repos = self.response.json()
            # data returned is a list of ‘repository’ entities
            repo_created_date = []
            for repo in repos:
                repo_created_date.append(repo["created_at"])
            return repo_created_date

    def getRepoHomepage(self):
        if self.response.status_code == 200:
            repos = self.response.json()
            # data returned is a list of ‘repository’ entities
            repo_homepage = []
            for repo in repos:
                repo_homepage.append(repo["homepage"])
            return repo_homepage

    def getRepoLists(self):
        if self.response.status_code == 200:
            list_name = self.getRepoName()
            list_created = self.getRepoCreatedDate()
            list_pushed = self.getRepoLastPushed()
            list_homepage = self.getRepoHomepage()
            repo_list = zip(
                list_name, list_created, list_pushed, list_homepage
            )
            return repo_list


class GitHubRepo:
    def __init__(self, repo_full_name):
        self.name = repo_full_name
        self.response = requests.get(
            "https://api.github.com/repos/"
            + repo_full_name
            + "/commits?per_page=5"
        )

    def getCommitHash(self):
        if self.response.status_code == 200:
            commits = self.response.json()
            commit_hash = []
            for commit in commits:
                commit_hash.append(commit["sha"])
            return commit_hash

    def getCommitAuthor(self):
        if self.response.status_code == 200:
            commits = self.response.json()
            commit_author = []
            for commit in commits:
                commit_author.append(commit["commit"]["author"]["name"])
            return commit_author

    def getCommitDate(self):
        if self.response.status_code == 200:
            commits = self.response.json()
            commit_date = []
            for commit in commits:
                commit_date.append(commit["commit"]["author"]["date"])
            return commit_date

    def getCommitMessage(self):
        if self.response.status_code == 200:
            commits = self.response.json()
            commit_message = []
            for commit in commits:
                commit_message.append(commit["commit"]["message"])
            return commit_message

    # NOT DONE
    def getRepoCommitsLists(self):
        if self.response.status_code == 200:
            commits = self.response.json()
            commit_list = []
            for commit in commits:
                hash = commit["sha"]
                author = commit["commit"]["author"]["name"]
                date = commit["commit"]["author"]["date"]
                commit_message = commit["commit"]["message"]
                commit_list.append(zip(hash, author, date, commit_message))
            return commit_list
