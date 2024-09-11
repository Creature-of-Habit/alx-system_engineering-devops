#!/usr/bin/python3
''' 
Recursive function that queries the Reddit API.
Returns a list containing the titles of all hot articles for a given subreddit
'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''
    Queries the Reddit API recursively.
    Returns a list of the titles of all hot articles for a given subreddit

    Args:
        subreddit (str): Given subreddit
        hot_list (list): list of all the hot titles
        after (str): a pointer to the next page of the given subreddit

    Returns:
        List of all the titles of the hot articles for the given subreddit
    '''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    header = {'User-Agent': '1-top_ten'}
    response = requests.get(url=url, headers=header,
                            params={'after': after}, allow_redirects=False, timeout=10)

    if response.status_code != 200:
        return None

    else:
        resp = response.json().get('data')
        r_data = resp.get('children')
        after = resp.get('after')

        for res in r_data:
            data = res.get('data')
            title = data.get('title')
            print(title)
            hot_list.append(title)

        if after is not None:
            return recurse(subreddit=subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list
