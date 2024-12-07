def is_valid(amount: int, current:int, operands: list, operations: dict[str, any]) -> int:
    
    if len(operands) == 0:
        return amount if current == amount else 0

    for operation in operations:
        if is_valid(amount, operations[operation](current, operands[0]), operands[1:], operations):
            return amount

    return 0

def main() -> None:
    amount_part1 = 0
    amount_part2 = 0
    operations = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
    }
    operations_with_concat = {**operations, "||": lambda x, y: int(str(x) + str(y))}
    with open("input.txt") as file:
        data = file.read().splitlines()
        for line in data:
            [amount, operands] = line.split(":")
            amount = int(amount)
            operands =  [int(operand) for operand in operands.split(" ")[1:]]
            amount_part1 += is_valid(amount, 0, operands, operations)
            amount_part2 += is_valid(amount, 0, operands, operations_with_concat)
        print("Part 1:", amount_part1)
        print("Part 2:", amount_part2)
    
if __name__ == "__main__":
    main()