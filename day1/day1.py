def get_sorted_lists(data) -> tuple[list[int],list[int]]:
    first_array = []
    second_array = []

    with open("input.txt", "r") as file:
        data = file.read().splitlines()
        
        for line in data:
            [first, second] = line.split("   ")
            first_array.append(int(first))
            second_array.append(int(second))
    
    return first_array, second_array


def get_total_distance(first_array, second_array) -> int:
    total_distance = 0
    for idx in range(len(first_array)):
        total_distance += abs(first_array[idx] - second_array[idx])
    return total_distance


def get_silimarity_score(first_array, second_array) -> int:
    current_idx = 0
    similiarity_score = 0

    for number1 in first_array:
        repetition = 0
        while current_idx < len(second_array) and number1 >= second_array[current_idx]:
            if number1 == second_array[current_idx]:
                repetition += 1
            current_idx += 1

        similiarity_score += repetition * number1
    
    return similiarity_score
        

def main() -> None:
    first_array, second_array = get_sorted_lists("input.txt")

    first_array.sort()
    second_array.sort()

    print("Part 1: ", get_total_distance(first_array, second_array))
    print("Part 2: ", get_silimarity_score(first_array, second_array))
    

if __name__ == "__main__":
    main()