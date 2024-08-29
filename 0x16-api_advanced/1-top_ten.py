#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    header = {"User-Agent":"top_ten"}
    response = requests.get(url,headers=header,timeout=10)
    if response.status_code != 200:
        print("None")
