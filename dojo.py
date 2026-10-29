#!/usr/bin/env python3
"""Code Quest — Daily Coding Dojo from the API."""

import json
import urllib.request

QUEST_API = "https://jsonplaceholder.typicode.com/posts"


def daily_quest():
    with urllib.request.urlopen(QUEST_API, timeout=10) as r:
        posts = json.loads(r.read().decode("utf-8"))
    post = posts[0]
    return {"quest_id": post["id"], "quest_text": post["title"], "hint": post["body"]}


def main():
    print(json.dumps(daily_quest(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
