#!/usr/bin/python3
"""
This is a module docstring
"""
import requests
import csv


def fetch_posts():
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    return {
        "status_code": req.status_code,
        "posts": req.json(),
    }

def  fetch_and_print_posts():
    res = fetch_posts()
    print(f"Status Code: {res['status_code']}")

    for post in res['posts']:
        print(post["title"])


def fetch_and_save_posts():
    res = fetch_posts()

    posts = res['posts']

    with open("posts.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=posts[0].keys())
        writer.writeheader()
        writer.writerows(res['posts'])
