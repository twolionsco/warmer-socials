"""Sketch: metric collector sketch.

Recorded 2025-04-30. Move to its own module if it pans out.
Not imported anywhere yet.
"""
from __future__ import annotations

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


def truncate(text: str, n: int = 80) -> str:
    """Truncate to n chars with a trailing ellipsis."""
    if len(text) <= n:
        return text
    return text[: max(0, n - 1)].rstrip() + "…"
