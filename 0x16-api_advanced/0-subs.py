#!/usr/bin/python3
'''function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit/'''
import requests


def number_of_subscribers(subreddit):
'''Returns number of subscribers for a subreddit if subreddit is valid. Returns 0 for invalid subreddit'''
	response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
	if response.status_code == 200:
		return response.json()['data']['subscribers']
	else:
		return 0
