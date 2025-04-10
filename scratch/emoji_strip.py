"""Sketch: emoji stripping helper.

Recorded 2025-04-10. Notes-to-self while exploring options.
Not imported anywhere yet.
"""
from __future__ import annotations

def flatten(nested):
    """Flatten one level of an iterable of iterables."""
    return [x for inner in nested for x in inner]


def chunked(iterable, n: int):
    """Yield successive n-sized chunks from an iterable."""
    buf = []
    for item in iterable:
        buf.append(item)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf
