"""Sketch: post freshness scorer.

Recorded 2025-05-01. Move to its own module if it pans out.
Not imported anywhere yet.
"""
from __future__ import annotations

def normalize_text(text: str) -> str:
    """Lowercase, collapse whitespace, strip."""
    return " ".join(text.lower().split())


def safe_get(d: dict, *keys, default=None):
    """Walk nested dicts; return default if any key is missing."""
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def retry_with_backoff(fn, attempts=3, base_delay=0.5):
    """Run fn() with simple exponential backoff."""
    import time
    delay = base_delay
    for i in range(attempts):
        try:
            return fn()
        except Exception:
            if i == attempts - 1:
                raise
            time.sleep(delay)
            delay *= 2
