import itertools

Position = tuple[int, int]


def antinodes(
    node_1: Position, node_2: Position, _: list[list[str]]
) -> tuple[Position, Position]:
    offset = [abs(node_2[0] - node_1[0]), abs(node_2[1] - node_1[1])]

    if node_1[1] > node_2[1]:
        offset[1] *= -1

    return [
        (node_1[0] - offset[0], node_1[1] - offset[1]),
        (node_2[0] + offset[0], node_2[1] + offset[1]),
    ]


def multiple_antinodes(
    node_1: Position, node_2: Position, city: list[list[str]]
) -> tuple[Position, Position]:
    offset = [abs(node_2[0] - node_1[0]), abs(node_2[1] - node_1[1])]

    if node_1[1] > node_2[1]:
        offset[1] *= -1

    antinodes_list = []

    current_x_off = offset[0]
    current_y_off = offset[1]
    while in_bound((node_1[0] + current_x_off, node_1[1] + current_y_off), city):
        antinodes_list.append((node_1[0] + current_x_off, node_1[1] + current_y_off))
        current_x_off += offset[0]
        current_y_off += offset[1]

    current_x_off = offset[0]
    current_y_off = offset[1]
    while in_bound((node_2[0] - current_x_off, node_2[1] - current_y_off), city):
        antinodes_list.append((node_2[0] - current_x_off, node_2[1] - current_y_off))
        current_x_off += offset[0]
        current_y_off += offset[1]

    return antinodes_list


def in_bound(pos: Position, city: list[list[str]]) -> bool:
    return 0 <= pos[0] < len(city) and 0 <= pos[1] < len(city[0])


def get_antennas_position(city: list[list[str]]) -> dict[str, list[Position]]:
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


def get_antinodes_position(city: list[list[str]], method: any) -> list[list[int, int]]:
    antennas = get_antennas_position(city)

    antinodes_position = set()
    for key in antennas:
        for pair in itertools.combinations(antennas[key], 2):
            for antinode in method(pair[0], pair[1], city):
                if in_bound(antinode, city):
                    antinodes_position.add(antinode)

    return antinodes_position


def main():
    with open("input.txt") as file:
        data = file.read().splitlines()
        city = [list(line) for line in data]
        print("Part 1: ", len(get_antinodes_position(city, antinodes)))
        print("Part 2: ", len(get_antinodes_position(city, multiple_antinodes)))


if __name__ == "__main__":
    main()
