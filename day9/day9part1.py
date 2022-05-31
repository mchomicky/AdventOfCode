import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/9/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

data = [[int(point) for point in list(line.strip())] for line in data.strip().split('\n')]

numCols = len(data[0])
numRows = len(data)

# Pad all borders with 9 so we don't have to set up special cases for corners and edges
data.insert(0, [9] * numCols)
data.extend([[9] * numCols])

for row in data:
    row.insert(0, 9)
    row.extend([9])


numCols += 2
numRows += 2

riskScore = 0

for row in range(1, numRows - 1):
    for col in range(1, numCols - 1):
        if all([data[row][col] < neighbor for neighbor in [data[row-1][col], data[row][col-1], data[row][col+1], data[row+1][col]]]):
            riskScore += data[row][col] + 1

print(riskScore)
