def get_block_file(data: str) -> list[str]:
    file_id = 0
    result = []
    for index, block in enumerate(data):
            is_file = index % 2 == 0
            repeat_value = file_id if is_file else '.'
            for _ in range(int(block)):
                result.append(repeat_value)

            if is_file:
                file_id += 1
            
    return result


def calculate_checksum(block_files: list[str]) -> int:
    only_files = list(filter(lambda x: x != '.',  block_files))

    last_index_files= -1
    checksum = 0
    for index, block in enumerate(block_files):
        if index >= len(only_files):
            break
        if block != '.':
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

def main() -> None:
    solve_part1()


main()