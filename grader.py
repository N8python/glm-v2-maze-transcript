"""Reference evaluator for the maze mapping task."""
from pathlib import Path

import numpy as np

# ASCII codes for wall, open path, start, exit
SYMBOL_CODES = np.array([35, 47, 83, 69], dtype=np.uint8)


def render_maze(cells):
    """Convert the evaluator's numeric grid to submission text."""
    if cells.ndim != 2 or cells.dtype.kind not in "iu":
        raise ValueError("Expected a two-dimensional integer grid")
    if cells.min() < 0 or cells.max() >= len(SYMBOL_CODES):
        raise ValueError("Unknown cell value")
    return "\n".join(
        row.tobytes().decode("ascii") for row in SYMBOL_CODES[cells]
    )


def grade(submission_path="/app/maze_map.txt"):
    maze_path = Path(__file__).resolve().with_name("maze.npy")
    cells = np.load(maze_path, allow_pickle=False)
    expected = render_maze(cells)
    submission = Path(submission_path)
    if not submission.is_file():
        return 0.0
    actual = submission.read_text(encoding="utf-8").rstrip("\r\n")
    return float(actual == expected)


if __name__ == "__main__":
    print(grade())
