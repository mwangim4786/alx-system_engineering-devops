#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def top_ten(subreddit):
    """Request titles of the first ten hot posts of a 
    givensubreddit from Reddit API
    """
    # set custom user-agent
    user_agent = '1-top_ten'
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print('None')
    else:
        # load response unit from json
        data = r.json()['data']
        # extract list of pages
        posts = data['children']
        for post in posts:
            print(post['data']['title'])
