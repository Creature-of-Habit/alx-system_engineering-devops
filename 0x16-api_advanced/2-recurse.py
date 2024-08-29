#!/usr/bin/python3
''' Recursive function that queries the Reddit API.
Returns a list containing the titles of all hot articles for a given subreddit'''
import requests

def recurse(subreddit, hot_list=[]):