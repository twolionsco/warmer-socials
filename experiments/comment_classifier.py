"""Sketch: comment classifier sketch.

Recorded 2025-10-31. Move to its own module if it pans out.
Not imported anywhere yet.
"""
from __future__ import annotations

def slugify(text: str) -> str:
    """Naive slugifier suitable for filenames."""
    keep = "abcdefghijklmnopqrstuvwxyz0123456789-_"
    return "".join(c if c in keep else "-" for c in text.lower()).strip("-")


def flatten(nested):
    """Flatten one level of an iterable of iterables."""
    return [x for inner in nested for x in inner]
