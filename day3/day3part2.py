import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/3/input',
                   headers={'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

# First, split raw text into a list and remove the empty string
data = res.text.split('\n')
while '' in data:
    data.remove('')


def calcO2Rating(vals):
    #vals = list(vals)
    i = 0
    while len(vals) > 1:
        bits = list(map(lambda x: x[i], vals))
        if bits.count('1') >= bits.count('0'):
            vals = list(filter(lambda y: y[i] == '1', vals))
        else:
            vals = list(filter(lambda y: y[i] == '0', vals))
        i += 1
    return vals[0]


def calcCO2Rating(vals):
    #vals = list(vals)
    i = 0
    while len(vals) > 1:
        bits = list(map(lambda x: x[i], vals))
        if bits.count('1') < bits.count('0'):
            vals = list(filter(lambda y: y[i] == '1', vals))
        else:
            vals = list(filter(lambda y: y[i] == '0', vals))
        i += 1
    return vals[0]


o2 = calcO2Rating(data)

co2 = calcCO2Rating(data)

print(int(o2, 2) * int(co2, 2))
