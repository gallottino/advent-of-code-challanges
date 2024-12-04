
def out_of_bound(map: list[list[str]], row_index, col_index):
    max_row = len(map)
    max_col = len(map[0])

    return (
        row_index < 0 or 
        col_index < 0 or 
        row_index >= max_row or 
        col_index >= max_col
    )

def is_pattern(
    map: list[list[str]], 
    row_index, col_index,
    offset: list[int,int],
    pattern: list[str]
) -> int:
    if len(pattern) <= 0:
        return 1
    
    if out_of_bound(map, row_index, col_index):
        return 0
    
    if map[row_index][col_index] != pattern[0]:
        return 0

    [row_off, col_off] = offset
    return is_pattern(
        map,
        row_index + row_off,
        col_index + col_off,
        offset,
        pattern=pattern[1:]
    )

def get_pattern_occurrencies(map, row_index, col_index, pattern) -> int:
    offsets=[
        [-1,-1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]
    occurrencies = 0
    for offset in offsets:
        occurrencies += is_pattern(
            map,
            row_index, col_index,
            offset,
            pattern
        )
    return occurrencies

def solve(map: list[list[str]]) -> int:
    total = 0

    pattern = ["X", "M", "A", "S"]
    for row_index, row in enumerate(map):
        for col_index, value in enumerate(row):
            if value == pattern[0]:
                total += get_pattern_occurrencies(map, row_index, col_index, pattern)

    return total

def main():
    with open("input.txt") as file:
        data = file.read().splitlines()
        result_1 = solve([list(line) for line in data])
        print("Part 1: ", result_1)

if __name__ == "__main__":
    main()