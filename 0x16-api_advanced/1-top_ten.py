#!/usr/bin/python3
''' Function that queries the Reddit API.
Prints the titles of the first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    '''
    Queries Reddit API and returns top ten hot topics.

    Args:
        Subreddit(str): subreddit

    Returns:
        List: Top ten hot topics if subreddit is valid, otherwise 0

    '''
    url = f'http://www.reddit.com/r/{subreddit}/hot.json'
    # header = {"User-Agent": "Hot_ten"}
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        hot_titles = []
        for post in posts[:10]:
            title = post.get('data', {}).get('title', 'No title')
            print(title)
            hot_titles.append(title)
        return hot_titles
    else:
        print(None)
        return 0  # Return 0 if the subreddit is invalid
