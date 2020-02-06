#!/usr/bin/python3
"""# subs of subreddit"""
import requests
import sys


def top_ten(subreddit):
    """# 10 hots"""
    try:
        head = {"User-Agent": "Teslothorcha"}
        redit_req = requests.get(
            'https://api.reddit.com/r/{}/hot?sort=hot&limit=10'.format(
            subreddit),
            headers=head)
        if redit_req.status_code == 404:
            return 0
        info = redit_req.json()
        num_hot = info['data']['children']
        for out in num_hot:
            print(out['data']['title'])
    except:
        print('None')
