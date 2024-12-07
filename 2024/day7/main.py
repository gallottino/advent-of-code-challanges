
def is_valid(amount: int, current:int, operands: list) -> int:
    if len(operands) == 0:
        return amount if current == amount else 0

    if is_valid(amount, current + operands[0], operands[1:]):
        return amount
    if is_valid(amount, current * operands[0], operands[1:]):
        return amount

    return 0

def is_valid_with_concat(amount: int, current:int, operands: list) -> int:
    if len(operands) == 0:
        return amount if current == amount else 0

    if is_valid_with_concat(amount, current + operands[0], operands[1:]):
        return amount
    if is_valid_with_concat(amount, current * operands[0], operands[1:]):
        return amount
    if is_valid_with_concat(amount, int(str(current) + str(operands[0])), operands[1:]):
        return amount

    return 0

def solve_part2(data: list[str]) -> int:
    total = 0
    for line in data:
        [amount, operands] = line.split(":")
        amount = int(amount)
        operands =  [int(operand) for operand in operands.split(" ")[1:]]
        total += is_valid_with_concat(amount, 0, operands)
    return total

def solve_part1(data: list[str]) -> int:
    total = 0
    for line in data:
        [amount, operands] = line.split(":")
        amount = int(amount)
        operands =  [int(operand) for operand in operands.split(" ")[1:]]
        total += is_valid(amount, 0, operands)
    return total

def main() -> None:
    with open("input.txt") as file:
        data = file.read().splitlines()
        print("Part 1:", solve_part1(data))
        print("Part 2:", solve_part2(data))
    
if __name__ == "__main__":
    main()