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
    response = requests.get(url=url, headers=headers,allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
