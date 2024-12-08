import itertools
    
Position = tuple[int, int]

def antinodes(node_1: Position, node_2: Position) -> tuple[Position, Position]:

    offset = [abs(node_2[0] - node_1[0]), abs(node_2[1] - node_1[1])]

    if node_1[1] > node_2[1]:
        offset[1] *= -1

    return [
        (node_1[0] - offset[0], node_1[1] - offset[1]),
        (node_2[0] + offset[0], node_2[1] + offset[1])
    ]

def in_bound(pos: Position, city: list[list[str]]) -> bool:
    return 0 <= pos[0] < len(city) and 0 <= pos[1] < len(city[0])

def get_antennas_position(city: list[list[str]]) -> dict[str,list[Position]]:
    antennas = {}
    for row_idx, row in enumerate(city):
        for col_idx, cell in enumerate(row):
            new_pos = (row_idx, col_idx)
            if cell != ".":
                if antennas.get(cell) is None:
                    antennas[cell] = [new_pos]
                else:
                    antennas[cell].append(new_pos)
    return antennas

def get_antinodes_position(city: list[list[str]]) -> list[list[int,int]]:

    antennas = get_antennas_position(city)
   
    antinodes_position = set()
    for key in antennas:
        for pair in itertools.combinations(antennas[key], 2):
            for antinode in antinodes(pair[0], pair[1]):
                if in_bound(antinode, city):
                    print(pair, antinode)
                    antinodes_position.add(antinode)

    return antinodes_position

def main():
   with open("input.txt") as file:
        data = file.read().splitlines()
        city = [list(line) for line in data]
        print("Part 1: ", len(get_antinodes_position(city)))

if __name__ == "__main__":
    main()