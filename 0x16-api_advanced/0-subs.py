#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
	response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
	if response.status_code == 200:
		return response.json()['data']['subscribers']
	else:
		return 0
