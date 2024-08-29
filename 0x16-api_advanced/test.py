import requests

url = 'http://www.reddit.com/r/bleach/hot.json'
# header = {"User": "Hot_ten"}
response = requests.get(url, allow_redirects=False)
print(response.status_code)
'''if response.status_code == 200:
    data = response.json()
    posts = data.get('data', {}).get('children', [])

    hot_titles = []
    for post in posts[:10]:
        title = post.get('data', {}).get('title', 'No title')
        hot_titles.append(title)

print(hot_titles)'''
