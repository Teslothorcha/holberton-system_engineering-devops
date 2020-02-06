#!/usr/bin/python3
"""# subs of subreddit"""
import requests
import sys


def recurse(subreddit, hot_list=[], e_q_s=None):
    """# 10 hots"""
    try:
        head = {"User-Agent": "Teslothorcha"}
        parm = {'t': 'all', 'after': e_q_s}
        redit_req = requests.get(
            'https://api.reddit.com/r/{}/hot'.format(
                subreddit), headers=head, params=parm)
        if redit_req.status_code == 404:
            return(None)
        info = redit_req.json()
        num_hot = info['data']['children']
        for out in num_hot:
            hot_list.append(out['data']['title'])
        el_que_sigue = info['data']['after']
        if el_que_sigue:
            recurse(subreddit, hot_list, el_que_sigue)
        return hot_list
    except:
        return None
