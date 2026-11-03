# Maze mapping task

Explore the maze through `/app/maze_game.sh` and reconstruct its complete layout. You begin at the starting cell. Keep the interface process open while exploring; starting a new process resets your position.

## Interface

- `move N`, `move S`, `move E`, or `move W` moves one cell.
- You can batch movements as `move N & E & S`.
- Each movement returns `hit wall`, `moved`, or `reached exit`. Batch responses appear in the same order, separated by ` & `.
- Hitting a wall leaves your position unchanged. Reaching the exit does not end the session; continue until you have mapped the maze.
- `exit` closes the session.

## Submission

Write the completed map to `/app/maze_map.txt`, with one row per line, north at the top and west at the left. Use these characters:

- `#` for walls
- `.` for open paths
- `S` for the starting cell
- `E` for the exit

Every non-wall cell is reachable from the start. The complete grid is the smallest rectangle containing all reachable cells, padded by exactly one wall cell on each side. Include that complete border in your submission.

## Reference evaluator

`/app/grader.py` is provided as a read-only reference. You may read and inspect it freely. It is an exact copy of the evaluator used to score your submission. Evaluation runs against an identical copy, so modifying the local file will not change your score.

The evaluator’s `maze.npy` asset is only available in the evaluation environment and is not included in your workspace. Discover the layout through the movement interface; you do not need this asset to complete the task.
