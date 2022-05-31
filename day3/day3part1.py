import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/3/input',
                   headers={'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

# First, split raw text into a list and remove the empty string
data = res.text.split('\n')
while '' in data:
    data.remove('')

gamma = ''
epsilon = ''

for i in range(12):
    bits = list(map(lambda x: x[i], data))
    if bits.count('1') > bits.count('0'):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
