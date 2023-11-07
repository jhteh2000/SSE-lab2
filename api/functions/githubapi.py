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

    # def getRepoLists(self):
    #     if self.response.status_code == 200:
    #         list_name = self.getRepoName()
    #         list_pushes = self.getRepoLastPushed()
    #         repo_list = zip(list_name, list_pushes)
    #         return repo_list

    def getRepoLists(self):
        if self.response.status_code == 200:
            # store data as a list of ‘repository’ entities
            repos = self.response.json()

            # Define the keys you want to extract
            keys_to_extract = [
                "full_name",
                "created_at",
                "pushed_at",
                "homepage",
            ]

            # Initialize a 2D array to store the extracted data
            list_results = []

            # Iterate over each dictionary in the JSON data
            for item in repos:
                row = []  # Initialize a row to store values for this item

                # Extract the values for the specified keys
                for key in keys_to_extract:
                    if key in item:
                        row.append(item[key])
                    else:
                        row.append(None)
                        # If key is not present, add None to the row

                list_results.append(row)

            # Print the resulting 2D array
            for row in list_results:
                print(row)
        return list_results


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
