#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of a given
    subreddit from Reddit API
    """
    # set custom user-agent
    user_agent = 'Mozilla/5.0'
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    # load response unit from json
    data = r.json()['data']
    # extract list of pages
    pages = data['children']
    # extract data from first page
    page_data = pages[0]['data']
    # return number of subreddit subs
    return page_data['subscribers']
