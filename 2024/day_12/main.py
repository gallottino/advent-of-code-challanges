import copy


def in_bound(map: list[list[str]], current_pos: list[int]) -> bool:
    return 0 <= current_pos[0] < len(map) and 0 <= current_pos[1] < len(map[0])


current_region = []
def visit_region(map: list[list[(str, bool)]],current_pos: list[int], value: str) -> None:
    global current_region

    [current_row, current_col] = current_pos
    
    if not in_bound(map, current_pos):
        return
    
    if map[current_row][current_col][0] != value:
        return
    
       
    if map[current_row][current_col][1]:
        return
    
    map[current_row][current_col] = (value, True)
    current_region.append(current_pos)

    offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for offset in offsets:
        new_pos = [current_row + offset[0], current_col + offset[1]]
        visit_region(map, new_pos, value)


def solve_part1(region_map: list[list[(str, bool)]]) -> int:
    global current_region

    regions = []
    for row_idx, row in enumerate(region_map):
        for col_idx, cell in enumerate(row):
            current_region = []
            if cell[1] == False:
                current_region = []
                visit_region(region_map, [row_idx, col_idx], cell[0])
                if len(current_region) > 0:
                    regions.append(current_region)

    total = 0
    for region in regions:
        total += calculate_price(region)

    return total

def get_regions(region_map: list[list[(str, bool)]]) -> list[list[list[(str, bool)]]]:
    global current_region

    regions = []
    for row_idx, row in enumerate(region_map):
        for col_idx, cell in enumerate(row):
            current_region = []
            if cell[1] == False:
                current_region = []
                visit_region(region_map, [row_idx, col_idx], cell[0])
                if len(current_region) > 0:
                    regions.append(current_region)

    return regions

def solve_part2(regions: list[list[(str, bool)]]) -> int:
    global current_region

    
    region_list = get_regions(regions)
    total = 0
    for region in region_list:

        area = len(region)
        corners = count_corners(region, regions)
        total += area * corners

    return total


def count_corners(region: list[list[str]], regions) -> int:
    corners = 0

    valid_outer_corners = [
        # TOP-LEFT
        [[0, -1],[-1, -1],[-1, 0]],
        # TOP-RIGHT
        [[0, 1],[-1, 0],[-1 , 1]],
        # BOTTOM-LEFT
        [[0, -1],[1, -1],[1, 0]],
        # BOTTOM-RIGHT
        [[0, 1],[1, 0],[1, 1]]
    ]

    for block in region:
        [row_idx, col_idx] = block
        for corner in valid_outer_corners:
            is_corner = True
            for offset in corner:
                new_row = row_idx + offset[0]
                new_col = col_idx + offset[1]
                if [new_row, new_col] in region:
                    is_corner = False
                    break
            if is_corner:
                corners += 1


    valid_inner_corners = [
        # in region       out region
        [[-1, 1],         [0 , 1]],
        [[-1, -1],        [0, -1]],
        [[1, 1],          [0, 1]],
        [[1, -1],         [0, -1]]
    ]

    for block in region:
        [row_idx, col_idx] = block
        for corner in valid_inner_corners:
            is_corner = True
            
            offset = corner[0]
            new_row = row_idx + offset[0]
            new_col = col_idx + offset[1]
            if [new_row, new_col] not in region:
                is_corner = False
            
            offset = corner[1]
            new_row = row_idx + offset[0]
            new_col = col_idx + offset[1]
            if [new_row, new_col] in region:
                is_corner = False

            if is_corner:
                corners += 1

    return corners

def calculate_perimeter_region(region: list[list[(str, bool)]]) -> int:
    offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    total_perimeter = 0
    for _, block in enumerate(region):
            [row_idx, col_idx] = block
            for offset in offsets:
                new_row = row_idx + offset[0]
                new_col = col_idx + offset[1]
                if [new_row, new_col] not in region:
                    total_perimeter += 1
                
    return total_perimeter

def calculate_price(region: list[list[(str, bool)]]) -> int:
    area = len(region)
    price = area * calculate_perimeter_region(region)
    return price

def main() -> None: 

    with open("input.txt") as f:
        lines = f.read().splitlines()

        for i in range(len(lines)):
            lines[i] = [(char, False) for char in lines[i]]

        print("Part 1: ", solve_part1(copy.deepcopy(lines)))
        print("Part 2: ", solve_part2(copy.deepcopy(lines)))


if __name__ == "__main__":
    main()
