from utils.aoc import get_data_for

data = [list(map(lambda x: int(x), line.split())) for line in get_data_for(day=10)[:-1]]

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

starting = (None, None)
matrix = {}

for row in data:
    for col in row:
        match col:
            case "|":
                ...
            case "-":
                ...
            case "L":
                ...
            case "J":
                ...
            case "7":
                ...
            case "F":
                ...
            case ".":
                ...
            case "S":
                ...
