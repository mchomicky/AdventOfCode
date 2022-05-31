data = '3,4,3,1,2'

fish = [int(x) for x in data.strip().split(',')]

fishCounts = {}

for i in range(-1, 9):
    fishCounts[f'{i}_days'] = fish.count(i)

for i in range(256):
    for j in range(9):
        fishCounts[f'{j-1}_days'] = fishCounts[f'{j}_days']
    fishCounts['8_days'] = fishCounts['-1_days']
    fishCounts['6_days'] += fishCounts['8_days']

total = sum([v for k, v in fishCounts.items() if k != '-1_days'])
print(total)
