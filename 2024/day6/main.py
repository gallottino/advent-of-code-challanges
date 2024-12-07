directions_keys = [
    '^',
    '>',
    'v',
    '<'
]

directions = [
    [-1,  0],
    [ 0,  1],
    [ 1,  0],
    [ 0, -1]
]

def out_of_bound(maze: list[list[str]], row_idx, col_idx) -> bool:
    max_row = len(maze)
    max_col = len(maze[0])

    return (
        row_idx < 0 or 
        col_idx < 0 or 
        row_idx >= max_row or 
        col_idx >= max_col
    )

def get_next_direction(direction) -> int:
    return 0 if direction + 1 >= len(directions) else direction + 1

def check_direction(maze: list[list[str]], row_idx, col_idx, current_direction) -> int:
 
    [row_off, col_off] = directions[current_direction]
    if out_of_bound(maze, row_idx + row_off, col_idx + col_off):
        return current_direction
    
    next_direction = current_direction
    while maze[row_idx + row_off][col_idx + col_off] in ['#', 'O']:
        next_direction = get_next_direction(next_direction)
        [row_off, col_off] = directions[next_direction]

    return next_direction

def search_start_point(maze: list[list[str]]) -> list[int,int, int]:
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell in directions_keys:
                current_direction = directions_keys.index(cell)
                return [row_idx, col_idx, current_direction]

def try_solve(maze: list[list[str]],start_point: list[int,int], direction: int) -> int:
    [row_idx, col_idx] = start_point

    passed_yet = set()
    while not out_of_bound(maze, row_idx, col_idx):
        current_point = (row_idx, col_idx, direction)
        if current_point in passed_yet:
            return 0

        passed_yet.add((current_point))

        [row_off, col_off] = directions[direction]
        direction = check_direction(maze, row_idx, col_idx, direction)
        [row_off, col_off] = directions[direction]
        row_idx += row_off
        col_idx += col_off

    no_repeat = set()
    for [row, col, _] in passed_yet:
        no_repeat.add((row, col))
    
    return len(no_repeat)

def solve_part1(maze: list[list[str]], row_idx, col_idx, direction) -> int:
    return try_solve(maze, [row_idx, col_idx], direction)

def solve_part2(maze: list[list[str]], start_row, start_col, start_direction) -> int:

    obstacles = set()

    row_idx = start_row
    col_idx = start_col
    direction = start_direction

    while not out_of_bound(maze, row_idx, col_idx):

        prev = maze[row_idx][col_idx]
        maze[row_idx][col_idx] = "O"
        
        if try_solve(maze, [start_row, start_col], start_direction) == 0:
                obstacles.add((row_idx, col_idx))

        maze[row_idx][col_idx] = prev

        direction = check_direction(maze, row_idx, col_idx, direction)
        [row_off, col_off] = directions[direction]
        row_idx += row_off
        col_idx += col_off

    return len(obstacles)

def main() -> None:
    
    with open("input.txt") as file:
        maze = [list(line) for line in file.read().splitlines()]
        [row_idx, col_idx, direction] = search_start_point(maze)
        print("Part 1:", solve_part1(maze, row_idx, col_idx, direction))
        print("Part 2:", solve_part2(maze, row_idx, col_idx, direction))

if __name__ == "__main__":
    main()