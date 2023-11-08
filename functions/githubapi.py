import requests

# Authenticate with personal token for higher API rate limit
headers = {
    "Authorization": "token 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",
}


class GitHubUser:
    def __init__(self, username):
        self.username = username
        self.response = requests.get(
            "https://api.github.com/users/" + self.username,
            headers=headers,
        )

    def getFollowersCount(self):
        if self.response.status_code == 200:
            user = self.response.json()
            followers_count = user["followers"]
            return followers_count

    def getFollowingCount(self):
        if self.response.status_code == 200:
            user = self.response.json()
            following_count = user["following"]
            return following_count

    def getFollowers(self):
        self.response = requests.get(
            "https://api.github.com/users/" + self.username + "/followers",
            headers=headers,
        )
        if self.response.status_code == 200:
            followers = self.response.json()
            # data returned is a list of ‘repository’ entities
            list_followers = []
            for follower in followers:
                list_followers.append(follower["login"])
            list_avatar_url = []
            for follower in followers:
                list_avatar_url.append(follower["avatar_url"])
            return list_followers, list_avatar_url

    def getFollowing(self):
        self.response = requests.get(
            "https://api.github.com/users/" + self.username + "/following",
            headers=headers,
        )
        if self.response.status_code == 200:
            following = self.response.json()
            # data returned is a list of ‘repository’ entities
            list_following = []
            for follow in following:
                list_following.append(follow["login"])
            list_avatar_url = []
            for follow in following:
                list_avatar_url.append(follow["avatar_url"])
            return list_following, list_avatar_url


class GitHubUserRepo:
    def __init__(self, username):
        self.username = username
        self.response = requests.get(
            "https://api.github.com/users/" + self.username + "/repos",
            headers=headers,
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
            repo_list = zip(list_name, list_created, list_pushed, list_homepage)
            return repo_list


class GitHubRepo:
    def __init__(self, repo_full_name):
        self.name = repo_full_name
        self.response = requests.get(
            "https://api.github.com/repos/" + repo_full_name + "/commits?per_page=5",
            headers=headers,
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

    def getRepoCommitsLists(self):
        if self.response.status_code == 200:
            list_hash = self.getCommitHash()
            list_author = self.getCommitAuthor()
            list_date = self.getCommitDate()
            list_message = self.getCommitMessage()
            repo_list = zip(list_hash, list_author, list_date, list_message)
            return repo_list


# Check the rate limit
rlim_response = requests.get(
    "https://api.github.com/rate_limit",
    headers=headers,
)
if rlim_response.status_code == 200:
    rate_limit = rlim_response.json()
    print(rate_limit["resources"]["core"])
