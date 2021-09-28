#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, next_page=None):
    """return list containing titles of all hot articles"""
    headers = {
        "User-Agent": "0x16. API_advanced-e_kiminza"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 50, "next_page": next_page, "count": count}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    response_ = response.json().get("data")
    next_page = response_.get("next_page")
    count += response_.get("dist")
    children = response_.get("children")
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)
    if next_page is not None:
        return recurse(subreddit, hot_list, count, next_page)
    return hot_list
