#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
	response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
	print(response.status_code)
	if response.status_code == 200:
		return response.json()['data']['subscribers']
	else:
		return 0