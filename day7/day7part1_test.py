data = '16,1,2,0,4,2,7,1,2,14'

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
