
def is_valid(amount: int, current:int, operands: list) -> int:
    if len(operands) == 0:
        return amount if current == amount else 0

    if is_valid(amount, current + operands[0], operands[1:]):
        return amount
    if is_valid(amount, current * operands[0], operands[1:]):
        return amount

    return 0

def main() -> None:
    total = 0
    with open("input.txt") as file:
        data = file.read().splitlines()
        for line in data:
            [amount, operands] = line.split(":")
            amount = int(amount)
            operands =  [int(operand) for operand in operands.split(" ")[1:]]
            total += is_valid(amount, 0, operands)

    print("Part 1:", total)
if __name__ == "__main__":
    main()