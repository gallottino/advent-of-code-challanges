
def get_rules_set(rules: list[str]):
    rules_set = {}
    for rule in rules:
        [prev, next] = rule.split("|")
        next_list = rules_set[prev] if prev in rules_set.keys() else []
        next_list.append(next)
        rules_set[prev] = next_list[:]

    return rules_set

def check_line(line: list[str], rules_set: {int,list[int]}) -> int:
    prev_set = set()
    for page in line:
        if page in rules_set.keys():
            if not check_rule(prev_set, rules_set[page]):
                    return 0
        prev_set.add(page)
                
    return line[int(len(line)/2)]

def check_rule(prev_set, rule: list[int]):
    for value in rule:
        if value in prev_set:
            return False

    return True

def solve_part1(lines: list[list[str]], rules_set: {int,list[int]}) -> int:
    total = 0
    for line in lines:
        middle_value = check_line(line.split(","), rules_set)
        total += int(middle_value)
    return total

def check_line_try_fix_order(line: list[str], rules_set: {int,list[int]}) -> int:
    
    fixed = False
    prev_set = set()

    idx = -1  
    while idx < len(line) - 1: 
        idx += 1
        prev_set.add(line[idx])
        rule = rules_set[line[idx]] if line[idx] in rules_set.keys() else []
        
        if check_rule(prev_set, rule):
            continue 
        
        while idx >= 0 and not check_rule(prev_set, rule):

            line[idx - 1], line[idx] = line[idx], line[idx - 1]
            prev_set.remove(line[idx])
            idx -= 1

        if idx < 0:
            return 0
        
        fixed = True
    
    return 0 if not fixed else line[int(len(line)/2)]

def solve_part2(lines: list[list[str]], rules_set: {int,list[int]}) -> int:
    total = 0
    for line in lines:
        middle_value = check_line_try_fix_order(line.split(","), rules_set)
        total += int(middle_value)

    return total

def main() -> None:
    with open("input.txt") as file:
        data = file.read().splitlines()
        end_rules_idx = data.index("")
        rules = data[0:end_rules_idx]
        rules_set = get_rules_set(rules)

        lines = data[end_rules_idx+1:]
        print("Part 1: ", solve_part1(lines, rules_set))
        print("Part 2: ", solve_part2(lines, rules_set))

if __name__ == "__main__":
    main()