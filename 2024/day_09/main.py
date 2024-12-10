def get_block_file(data: str) -> list[str]:
    file_id = 0
    result = []
    for index, block in enumerate(data):
        is_file = index % 2 == 0
        repeat_value = file_id if is_file else "."
        for _ in range(int(block)):
            result.append(repeat_value)

        if is_file:
            file_id += 1

    return result


def calculate_checksum(block_files: list[str]) -> int:
    only_files = list(filter(lambda x: x != ".", block_files))

    last_index_files = -1
    checksum = 0
    for index, block in enumerate(block_files):
        if index >= len(only_files):
            break
        if block != ".":
            checksum += index * block
        else:
            checksum += index * only_files[last_index_files]
            last_index_files -= 1

    return checksum


def solve_part1() -> None:
    with open("input.txt") as file:
        data = file.read()
        block_files = get_block_file(data)
        print("Part 1: ", calculate_checksum(block_files))


def count_spaces(index: int, block_files: list[str]) -> int:
    count = 0
    while index < len(block_files) and block_files[index] == ".":
        count += 1
        index += 1
    return count


def get_files_map(block_files: list[str]) -> dict[str, int]:
    map = {}
    for index, file in enumerate(block_files):
        if file != ".":
            if file not in map:
                map[file] = [index, 0]
            [fileIdx, size] = map[file]
            map[file] = [fileIdx, size + 1]
    return map


def calculate(list: list[str]) -> int:
    return sum(
        [index * int(block) if block != "." else 0 for index, block in enumerate(list)]
    )


def calculate_checksum_2(block_files: list[str]) -> int:
    files_map = get_files_map(block_files)
    files_map = dict(sorted(files_map.items(), reverse=True))

    for fileId, [fileIdx, size] in files_map.items():
        found = False
        index = 0
        while index < fileIdx and not found:
            if block_files[index] == ".":
                spaces = count_spaces(index, block_files)
                if spaces >= size:
                    found = True
                    for i in range(size):
                        block_files[fileIdx + i] = "."
                        block_files[index + i] = fileId
                    index += size
            index += 1

    return calculate(block_files)


def solve_part2() -> None:
    with open("input.txt") as file:
        data = file.read()
        block_files = get_block_file(list(data))
        print("Part 2: ", calculate_checksum_2(block_files))


def main() -> None:
    solve_part1()
    solve_part2()


main()
