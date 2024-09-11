#!/usr/bin/python3
'''
Recursive function that queries the Reddit API.
Parses the title of all the hot articles
Prints a sorted count of given keywords
Keywords are case-insensitive and delimited by spaces
'''

import requests


def count_words(subreddit, word_list, after="", results={}):
    '''
    Function that queries the reddit API.
    Parses the a list of given keywords(titles of hot articles)
    Prints a list of word count in the given subreddit

    Args:
        subreddit (str): given subreddit

        wordlist (list): keywords case-insensitive and delimited by spaces

    Returns:
        void
    '''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    header = {'User-Agent': '1-top_ten'}
    param = {'after': after}
    response = requests.get(url=url, headers=header,
                            params=param, allow_redirects=False, timeout=10)
    if response.status_code == 200:
        resp = response.json().get('data')
        r_data = resp.get('children')
        after = resp.get('after')

        for res in r_data:
            data = res.get('data')
            title = data.get('title')
            print(title)
        if after is not None:
            return recurse(subreddit=subreddit, hot_list=hot_list, after=after)
        else:
            return results
