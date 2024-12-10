def in_bounds(row_idx: int, col_idx: int, mount: list[str]) -> bool:
    return 0 <= row_idx < len(mount) and 0 <= col_idx < len(mount[0])


def check_trail(
    current_pos: list[int, int], mount: list[str], next_value: int, ends: set | list
) -> None:
    offsets = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]

    [row_idx, col_idx] = current_pos
    if not in_bounds(row_idx, col_idx, mount):
        return

    current_value = int(mount[row_idx][col_idx])
    if current_value != next_value:
        return

    if current_value == next_value and current_value == 9:
        if type(ends) is set:
            ends.add((row_idx, col_idx))
        else:
            ends.append((row_idx, col_idx))
        return

    for offset in offsets:
        [row_offset, col_offset] = offset
        check_trail(
            [row_idx + row_offset, col_idx + col_offset], mount, next_value + 1, ends
        )

    return

def solve_part1(mount: list[list[str]]) -> int:
    total = 0
    for row_idx, row in enumerate(mount):
        for col_idx, cell in enumerate(row):
            if cell == "0":
                ends = set()
                check_trail([row_idx, col_idx], mount, 0, ends)
                total += len(ends)

    return total

def solve_part2(mount: list[list[str]]) -> int:
    total = 0
    for row_idx, row in enumerate(mount):
        for col_idx, cell in enumerate(row):
            if cell == "0":
                ends = []
                check_trail([row_idx, col_idx], mount, 0, ends)
                total += len(ends)

    return total

def main() -> None:
    with open("input.txt") as file:
        data = file.read().splitlines()
        mount = [list(row) for row in data]
        print("Part 1: ", solve_part1(mount))
        print("Part 2: ", solve_part2(mount))


if __name__ == "__main__":
    main()
