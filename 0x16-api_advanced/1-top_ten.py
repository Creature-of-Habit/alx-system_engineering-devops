
#!/usr/bin/python3
"""
Function that queries the Reddit API.
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    Prints the titles of the first 10 hot posts listed for a given subreddit

    Args:
        subreddit (str): The given subreddit

    Returns:
        void
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    header = {"User-Agent": "1-top_ten"}
    response = requests.get(url=url, headers=header, params={
                            "limit": 10}, allow_redirects=False)

    if response.status_code == 200:
        r_data = response.json().get("data").get("children")
        for res in r_data:
            data = res.get("data")
            title = data.get("title")
            print(title)
    else:
        print(None)
