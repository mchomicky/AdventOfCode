import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/6/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

fish = [int(x) for x in data.strip().split(',')]

for i in range(256):
    for j in range(len(fish)):
        if fish[j] > 0:
            fish[j] -= 1
        else:
            fish[j] = 6
            fish.append(8)

print(len(fish))
