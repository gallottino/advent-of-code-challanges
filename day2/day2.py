
def safe(line) -> bool:
    direction = line[1] - line[0] > 0
    for index, value in enumerate(line[1:]):
        diff = value - line[index]
        current_direction = diff > 0
        if (current_direction != direction) or (abs(diff) > 3 or abs(diff) < 1):
            return False

    return True

def safe_ignoring_one_level(line) -> bool:
    direction = line[1] - line[0] > 0    

    for index, value in enumerate(line[1:]):
        diff = value - line[index]
        current_direction = diff > 0

        if (current_direction != direction) or (abs(diff) > 3 or abs(diff) < 1):  
            [fixed_1, fixed_2, fixed_3] = [line[:], line[:], line[:]]

            fixed_1.pop(0)
            fixed_2.pop(index)
            fixed_3.pop(index + 1)

            return any(map(safe, [fixed_1, fixed_2, fixed_3]))
    
    return True

def redData(filename):
    lines = []
    with open(filename) as f:
        data = f.read().splitlines()
        for line in data:
            lines.append([int(value) for value in line.split(" ")])
    return lines

def main():
    data = redData("2024/day2/input.txt")

    total_safe_part_1 = 0
    total_safe_part_2 = 0
    for line in data:
        if safe(line):
            total_safe_part_1 += 1
        if safe_ignoring_one_level(line):
            total_safe_part_2 += 1
    
    print("Part 1: ", total_safe_part_1)
    print("Part 2: ", total_safe_part_2)

main()