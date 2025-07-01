"""Sketch: creator ranker prototype.

Recorded 2025-07-01. Park here; circle back later.
Not imported anywhere yet.
"""
from __future__ import annotations

def safe_get(d: dict, *keys, default=None):
    """Walk nested dicts; return default if any key is missing."""
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def truncate(text: str, n: int = 80) -> str:
    """Truncate to n chars with a trailing ellipsis."""
    if len(text) <= n:
        return text
    return text[: max(0, n - 1)].rstrip() + "…"


def slugify(text: str) -> str:
    """Naive slugifier suitable for filenames."""
    keep = "abcdefghijklmnopqrstuvwxyz0123456789-_"
    return "".join(c if c in keep else "-" for c in text.lower()).strip("-")
