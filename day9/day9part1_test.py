data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

data = [[int(point) for point in list(line.strip())] for line in data.strip().split('\n')]

numCols = len(data[0])
numRows = len(data)

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


for row in data:
    print(row)

print('\n')

for row in data[1:-1]:
    print(row[1:-1])

print(riskScore)
