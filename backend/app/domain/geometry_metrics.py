# -*- coding: utf-8 -*-
"""
Sample geometric calculation module (starter boilerplate).
"""

def calculate_bounding_box(coords: list):
    """Returns [min_x, min_y, max_x, max_y] from a list of coordinate pairs."""
    if not coords:
        return [0.0, 0.0, 0.0, 0.0]
    xs = [pt[0] for pt in coords]
    ys = [pt[1] for pt in coords]
    return [min(xs), min(ys), max(xs), max(ys)]
