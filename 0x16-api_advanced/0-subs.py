#!/usr/bin/python3
"""# subs of subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """# of
    subscribers"""
    try:
        head = {"User-Agent": "Teslothorcha"}
        redit_req = requests.get(
            'https://api.reddit.com/r/{}/about'.format(subreddit),
            headers=head)
        if redit_req.status_code == 404:
            return 0
        info = redit_req.json()
        num_subs = info['data']['subscribers']
        return num_subs
    except:
        return 0
