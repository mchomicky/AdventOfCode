import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/5/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

# 2D array in form of [['0,9', ' 5,9'], ['8,0', ' 0,8'] ... ]
data = [x.split('->') for x in data.split('\n')]

# 3D array in form of [[[0, 9], [5, 9]], [[8, 0], [0, 8]]]
for pair in range(len(data)):
    for coord in range(len(data[pair])):
        data[pair][coord] = [int(x) for x in data[pair][coord].strip().split(',')]

# Filter to just the horizontal or vertical lines
part1data = list(filter(lambda pair: pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1], data))

# Function to create empty diagram based on required width and height obtained from dataset
def create_blank_diagram(endpoints):
    width = 0
    height = 0
    for endpoint in endpoints:
        width = max(width, endpoint[0][0], endpoint[1][0])
        height = max(height, endpoint[0][1], endpoint[1][1])

    return [[0] * (width + 1) for i in range(height + 1)]


# Function to calculate all vertices from the endpoints
def calculate_vertices(endpoints):
    vertices = [endpoints[0]]
    x = endpoints[0][0]
    y = endpoints[0][1]

    while not (x == endpoints[1][0] and y == endpoints[1][1]):
        dx = endpoints[1][0] - x
        dy = endpoints[1][1] - y
        if dx != 0:
            x += int(dx/abs(dx))
        if dy != 0:
            y += int(dy/abs(dy))
        vertices.append([x, y])

    return vertices


# Function to mark each line on the diagram
def create_line_vertices(endpoints, diagram):
    for endpoint in endpoints:
        line = calculate_vertices(endpoint)
        for vertex in line:
            diagram[vertex[1]][vertex[0]] += 1

    return diagram


# Create the starting diagrams
start1 = create_blank_diagram(part1data)
start2 = create_blank_diagram(data)

# Run the vertex creation function, calculate the score for part1
end = create_line_vertices(part1data, start1)
positionValues = sum(end, [])
intersections = list(filter(lambda x: x >= 2, positionValues))
score = len(intersections)
print(f'Part 1: {score}')

# Run the vertex creation function, calculate the score for part1
end = create_line_vertices(data, start2)
positionValues = sum(end, [])
intersections = list(filter(lambda x: x >= 2, positionValues))
score = len(intersections)
print(f'Part 2: {score}')
