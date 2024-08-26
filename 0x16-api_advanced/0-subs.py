#!/usr/bin/python3
'''function that queries the Reddit API. 
Returns the number of subscribers for a given subreddit/'''
import requests


def number_of_subscribers(subreddit):
    '''Returns number of subscribers for a subreddit if subreddit is valid. 
    Returns 0 for invalid subreddit'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent":"0-subs"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    results = response.json().get("data")
    if results is None:
        return 0
    if response.status_code == 404:
        return 0
    return results.get("subscribers")