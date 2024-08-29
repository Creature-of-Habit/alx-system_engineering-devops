#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    # Set a custom User-Agent to avoid being blocked
    headers = {'User-Agent': 'MyRedditApp/0.1'}

    # Construct the URL for the subreddit's about page
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and if the subreddit exists
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0
    except requests.RequestException:
        # Return 0 if there's any error making the request
        return 0
