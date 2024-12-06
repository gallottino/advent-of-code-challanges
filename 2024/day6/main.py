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

def get_new_direction(maze: list[list[str]], row_idx, col_idx, current_direction) -> int:
    if not out_of_bound(maze, row_idx, col_idx) and maze[row_idx][col_idx] == '#':
        return current_direction + 1 if current_direction + 1 < len(directions) else 0

    return current_direction

def search_start_point(maze: list[list[str]]) -> list[int,int, int]:
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell in directions_keys:
                current_direction = directions_keys.index(cell)
                return [row_idx, col_idx, current_direction]
        
def count_x(maze: list[list[str]]) -> int:
    total_x = 0
    for _, row in enumerate(maze):
        for _, cell in enumerate(row):
            if cell == 'X':
                total_x += 1

    return total_x

def solve_part1(maze: list[list[str]], row_idx, col_idx, direction) -> int:
    
    while not out_of_bound(maze, row_idx, col_idx):
        maze[row_idx][col_idx] = "X"
        [row_off, col_off] = directions[direction]
        direction = get_new_direction(maze, row_idx + row_off, col_idx + col_off, direction)
        [row_off, col_off] = directions[direction]
        row_idx += row_off
        col_idx += col_off

    return count_x(maze)

def main() -> None:
    
    with open("input.txt") as file:
        maze = [list(line) for line in file.read().splitlines()]
        [row_idx, col_idx, direction] = search_start_point(maze)
        print("Part 1:", solve_part1(maze, row_idx, col_idx, direction))

if __name__ == "__main__":
    main()