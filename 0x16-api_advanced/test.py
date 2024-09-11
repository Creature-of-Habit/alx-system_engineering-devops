import requests
import sys
import json


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/top/.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print(f"Error: Received status code {r.status_code}")
        return

    try:
        data = r.json()
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON")
        print(f"Response content: {r.text}")
        return

    # Your code to process the JSON response
    # Example: print top ten posts
    for post in data['data']['children']:
        print(post['data']['title'])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Please provide a subreddit name as an argument.")
