testData = '''0,9 -> 5,9
8,0 -> 0,8 
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4 
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4 
0,0 -> 8,8
5,5 -> 8,2'''

# 2D array in form of [['0,9', ' 5,9'], ['8,0', ' 0,8'] ... ]
testData = [x.split('->') for x in testData.split('\n')]

# 3D array in form of [[['0', '9'], ['5', '9']], [['8', '0'], ['0', '8']]]
# testData = [[coord.strip().split(',')] for pair in testData for coord in pair]

# 3D array in form of [[[0, 9], [5, 9]], [[8, 0], [0, 8]]]
for pair in range(len(testData)):
    for coord in range(len(testData[pair])):
        testData[pair][coord] = [int(x) for x in testData[pair][coord].strip().split(',')]

part1data = list(filter(lambda pair: pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1], testData))

testEnds = [
    [[0, 9], [5, 9]],
    [[9, 4], [3, 4]],
    [[2, 2], [2, 1]],
    [[7, 0], [7, 4]],
    [[0, 9], [2, 9]],
    [[3, 4], [1, 4]]
]


# Function to create empty diagram based on required width and height obtained from dataset
def create_blank_diagram(endpoints):
    width = 0
    height = 0
    for pair in endpoints:
        width = max(width, int(pair[0][0]), int(pair[1][0]))
        height = max(height, int(pair[0][1]), int(pair[1][1]))

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
    for pair in endpoints:
        line = calculate_vertices(pair)
        for vertex in line:
            diagram[vertex[1]][vertex[0]] += 1

    return diagram


# Create the starting diagram
start = create_blank_diagram(testEnds)

# Run the vertex creation function, calculate the score
end = create_line_vertices(testEnds, start)
positionValues = sum(end, [])
intersections = list(filter(lambda x: x >= 2, positionValues))
score = len(intersections)
print(score)
