import requests


class GitHubUser:
    def __init__(self, username):
        self.username = username
        self.response = requests.get(
            "https://api.github.com/users/" + username + "/repos"
        )

    def getRepoLists(self):
        if self.response.status_code == 200:
            # store data as a list of ‘repository’ entities
            repos = self.response.json()

            # Define the keys you want to extract
            keys_to_extract = ["full_name", "created_at",
                               "pushed_at", "homepage"]

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
