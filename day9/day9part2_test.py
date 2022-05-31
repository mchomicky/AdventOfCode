data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

data = [[int(point) for point in list(line.strip())] for line in data.strip().split('\n')]


def find_low_points(data_arr):
    num_cols = len(data_arr[0])
    num_rows = len(data_arr)

    data_arr.insert(0, [9] * num_cols)
    data_arr.extend([[9] * num_cols])

    for row in data:
        row.insert(0, 9)
        row.extend([9])

    num_cols += 2
    num_rows += 2

    low_points = []

    for row in range(1, num_rows - 1):
        for col in range(1, num_cols - 1):
            if all([data[row][col] < neighbor for neighbor in [data[row - 1][col], data[row][col - 1], data[row][col + 1], data[row + 1][col]]]):
                low_points.append([row, col])

    return low_points


def find_basin_size(curr_point, data_arr, prev_point_val=float('-inf'), visited_points=[]):
    size = 0
    curr_point_val = data_arr[curr_point[0]][curr_point[1]]

    if curr_point_val == 9 or curr_point_val < prev_point_val:
        return 0
    else:
        if curr_point not in visited_points:
            size += 1
            visited_points.append(curr_point)
        # Move up from curr_point
        size += find_basin_size([curr_point[0] - 1, curr_point[1]], data_arr, curr_point_val, visited_points)
        # Move right from curr_point
        size += find_basin_size([curr_point[0], curr_point[1] + 1], data_arr, curr_point_val, visited_points)
        # Move down from curr_point
        size += find_basin_size([curr_point[0] + 1, curr_point[1]], data_arr, curr_point_val, visited_points)
        # Move left from curr_point
        size += find_basin_size([curr_point[0], curr_point[1] - 1], data_arr, curr_point_val, visited_points)

    return size


lowPoints = find_low_points(data)


print(lowPoints)
print(data[lowPoints[0][0]][lowPoints[0][1]])
print(find_basin_size(lowPoints[3], data))
