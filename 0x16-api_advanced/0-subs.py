#!/usr/bin/python3
'''
Function that queries the Reddit API.
Returns the number of subscribers for a given subreddit.
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API.
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    '''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': '0-subs.py'}

    response = requests.get(url=url, headers=header,
                            allow_redirects=False, timeout=10)
    if response.status_code == 200:
        res = response.json()
        subs = res.get('data').get('subscribers')
        return subs
    else:
        return 0
