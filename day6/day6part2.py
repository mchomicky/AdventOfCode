import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/6/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

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
