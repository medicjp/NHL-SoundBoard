#!/usr/bin/env python3
"""Wrap index.html (the artifact source) into a standalone page that opens offline from disk."""
from pathlib import Path
src = Path(__file__).with_name("index.html").read_text()
head, sep, body = src.partition('<div class="flash"')
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head + '</head>\n<body>\n' + sep + body + '\n</body>\n</html>\n')
Path(__file__).with_name("nhl-soundboard.html").write_text(page)
print("wrote nhl-soundboard.html", len(page)//1024, "KB")
