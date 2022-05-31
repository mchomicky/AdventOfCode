import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/9/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

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


def find_basin_size(curr_point, data_arr, visited_points=[]):
    size = 0
    curr_point_val = data_arr[curr_point[0]][curr_point[1]]

    if curr_point not in visited_points:
        size += 1
        visited_points.append(curr_point)
    # Move up from curr_point
    up = [curr_point[0] - 1, curr_point[1]]
    if 9 > data_arr[up[0]][up[1]] > curr_point_val:
        size += find_basin_size(up, data_arr, visited_points)
    # Move right from curr_point
    right = [curr_point[0], curr_point[1] + 1]
    if 9 > data_arr[right[0]][right[1]] > curr_point_val:
        size += find_basin_size(right, data_arr, visited_points)
    # Move down from curr_point
    down = [curr_point[0] + 1, curr_point[1]]
    if 9 > data_arr[down[0]][down[1]] > curr_point_val:
        size += find_basin_size(down, data_arr, visited_points)
    # Move left from curr_point
    left = [curr_point[0], curr_point[1] - 1]
    if 9 > data_arr[left[0]][left[1]] > curr_point_val:
        size += find_basin_size(left, data_arr, visited_points)

    return size


lowPoints = find_low_points(data)

scores = []

for point in lowPoints:
    scores.append(find_basin_size(point, data))

scores.sort()
print(scores[-1] * scores[-2] * scores[-3])
