import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/2/input',
                   headers={'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

# First, split raw text into a list and remove the empty string
data = res.text.split('\n')
while '' in data:
    data.remove('')

# Each list member also needs to be split into the direction and the value
data = list(map(lambda x: x.split(), data))

pos = 0
depth = 0

for x in data:
    if x[0] == 'forward':
        pos += int(x[1])
    elif x[0] == 'down':
        depth += int(x[1])
    elif x[0] == 'up':
        depth -= int(x[1])

print(pos * depth)