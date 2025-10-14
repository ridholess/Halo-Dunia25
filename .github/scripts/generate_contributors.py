#!/usr/bin/env python3
"""
Generate contributors HTML and replace markers in README.md
"""
import os
import sys
import json
from typing import List
from urllib import request, error

REPO = os.environ.get("GITHUB_REPOSITORY", "ridholess/Halo-Dunia25")
TOKEN = os.environ.get("GITHUB_TOKEN")
README_PATH = os.environ.get("INPUT_README_PATH", "README.md")
MARKER_START = "<!-- readme: contributors -start -->"
MARKER_END = "<!-- readme: contributors -end -->"
PER_PAGE = 100
COLUMNS = int(os.environ.get("INPUT_COLUMNS_PER_ROW", "8"))
IMG_SIZE = int(os.environ.get("INPUT_IMAGE_SIZE", "100"))


def get_contributors(repo: str, token: str) -> List[dict]:
    contributors = []
    page = 1
    base_url = f"https://api.github.com/repos/{repo}/contributors?per_page={PER_PAGE}"
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    while True:
        url = base_url + f"&page={page}"
        req = request.Request(url, headers=headers)
        try:
            with request.urlopen(req) as resp:
                if resp.status != 200:
                    raise SystemExit(f"GitHub API error {resp.status}: {resp.read().decode()}")
                data = json.load(resp)
        except error.HTTPError as e:
            raise SystemExit(f"GitHub API error {e.code}: {e.read().decode()}")

        if not data:
            break
        contributors.extend(data)
        if len(data) < PER_PAGE:
            break
        page += 1
    return contributors


def build_html(contributors: List[dict]) -> str:
    html = ["<table>\n<tbody>\n<tr>\n"]
    count = 0
    for c in contributors:
        login = c.get("login")
        name = c.get("login")
        avatar = c.get("avatar_url")
        profile = c.get("html_url")
        # Try to use name if available (public name requires extra API call - skip)
        cell = (
            f'    <td align="center">\n'
            f'        <a href="{profile}">\n'
            f'            <img src="{avatar}&s={IMG_SIZE}" width="{IMG_SIZE};" alt="{login}"/>\n'
            f'            <br />\n'
            f'            <sub><b>{name}</b></sub>\n'
            f'        </a>\n'
            f'    </td>\n'
        )
        html.append(cell)
        count += 1
        if count % COLUMNS == 0:
            html.append("</tr>\n<tr>\n")
    html.append("</tr>\n</tbody>\n</table>\n")
    return "".join(html)


def replace_readme(readme_path: str, new_block: str):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    start = content.find(MARKER_START)
    end = content.find(MARKER_END)
    if start == -1 or end == -1:
        raise SystemExit("Markers not found in README.md")
    before = content[: start + len(MARKER_START)]
    after = content[end:]
    new_content = before + "\n" + new_block + "\n" + after
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    if not TOKEN:
        print("Warning: GITHUB_TOKEN not provided; API rate limits may apply.")
    contributors = get_contributors(REPO, TOKEN)
    html = build_html(contributors)
    replace_readme(README_PATH, html)
    print(f"Updated {README_PATH} with {len(contributors)} contributors")


if __name__ == "__main__":
    main()
