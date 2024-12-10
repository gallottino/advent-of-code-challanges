def get_number(tokens, start_idx, end_char) -> list[int, int]:
    number_str = []
    current_idx = start_idx
    while current_idx < len(tokens):
        current_value = tokens[current_idx]
        if current_value.isdigit():
            number_str.append(current_value)
        elif current_value == end_char:
            break
        else:
            return [-1, current_idx]
        current_idx += 1

    number = int("".join(number_str))
    return [number, current_idx]


def mul_pattern(tokens, start_idx) -> list[int, int]:
    current_idx = start_idx

    matched = match_pattern(tokens, start_idx, pattern="mul(")

    if not matched:
        return [0, current_idx]

    [first_number, current_idx] = get_number(tokens, current_idx + 4, ",")
    if first_number < 0:
        return [0, current_idx]

    [second_number, current_idx] = get_number(tokens, current_idx + 1, ")")
    if second_number < 0:
        return [0, current_idx]

    return [first_number * second_number, current_idx]


# I don't want to use regular expression
def match_pattern(tokens, start_idx, pattern="") -> bool:
    current_idx = start_idx
    pattern_list = list(pattern)
    while current_idx < len(tokens) and len(pattern_list) > 0:
        if tokens[current_idx] != pattern_list[0]:
            return False
        pattern_list.pop(0)
        current_idx += 1
    return True


def solve_part2(tokens) -> int:
    idx = 0
    total_amount = 0
    do = True
    while idx < len(tokens):
        if tokens[idx] == "d":
            if match_pattern(tokens, idx, pattern="don't()"):
                do = False
            elif match_pattern(tokens, idx, pattern="do()"):
                do = True
        if do and tokens[idx] == "m":
            [amount, idx] = mul_pattern(tokens, idx)
            total_amount += amount
        idx += 1
    return total_amount


def solve_part1(tokens) -> int:
    idx = 0
    total_amount = 0
    while idx < len(tokens):
        if tokens[idx] == "m":
            [amount, idx] = mul_pattern(tokens, idx)
            total_amount += amount
        idx += 1
    return total_amount


def main() -> None:
    with open("input.txt") as file:
        data = file.read()
        result_part1 = solve_part1(list(data))
        result_part2 = solve_part2(list(data))
        print("Part 1: ", result_part1)
        print("Part 2: ", result_part2)


if __name__ == "__main__":
    main()
