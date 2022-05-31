import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/7/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

crabPositions = [int(x) for x in data.strip().split(',')]


def calc_fuel_cost(pos, arr):
    fuel_cost = 0
    for i in arr:
        fuel_cost += abs(pos - i)

    return fuel_cost


def calc_least_fuel_cost(arr):
    fuel_cost = float('inf')
    for pos in arr:
        cost_to_pos = calc_fuel_cost(pos, arr)
        if cost_to_pos < fuel_cost:
            fuel_cost = cost_to_pos

    return fuel_cost


print(calc_least_fuel_cost(crabPositions))
