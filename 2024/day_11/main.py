cache = {}
def number_of_stone(value: int, steps: int) -> int:
    global cache
    value_str = str(value)

    if (value, steps) in cache:
        return cache[(value, steps)]

    if steps == 0:
        return 0

    if value == 0:
        res = number_of_stone(1, steps - 1)
        cache[(value, steps)] = res
        return res
        
    elif len(value_str) % 2 == 0:
        first_half = int("".join(value_str[:len(value_str) // 2]))
        second_half = int("".join(value_str[len(value_str) // 2:]))
        res = 1 + number_of_stone(first_half, steps - 1) + number_of_stone(second_half, steps - 1)
        cache[(value, steps)] = res
        return res

    else:
        res = 0 + number_of_stone(value * 2024, steps - 1)
        cache[(value, steps)] = res
        return res

    
def main() -> None:

    with open("input.txt") as file:
        data = file.read().split(" ")

        total_1 = len(data)
        total_2 = len(data)
        for value in data:
            total_1 += number_of_stone(int(value), 25)
            total_2 += number_of_stone(int(value), 75)

        print("Part 1: ", total_1)
        print("Part 2: ", total_2)
        

if __name__ == "__main__":
    main()