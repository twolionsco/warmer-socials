"""Sketch: language detector helper.

Recorded 2025-10-01. Quick sketch; not wired in.
Not imported anywhere yet.
"""
from __future__ import annotations

def flatten(nested):
    """Flatten one level of an iterable of iterables."""
    return [x for inner in nested for x in inner]


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


def clamp(value, lo, hi):
    """Clamp value into [lo, hi]."""
    return max(lo, min(hi, value))
