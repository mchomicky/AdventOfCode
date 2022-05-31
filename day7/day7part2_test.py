import requests
import math

data = '16,1,2,0,4,2,7,1,2,14'

crabPositions = [int(x) for x in data.strip().split(',')]


def calc_fuel_cost(pos, arr):
    fuel_cost = 0
    for i in arr:
        base_cost = abs(pos - i)
        fuel_cost += base_cost + sum(range(base_cost))

    return fuel_cost


def calc_least_fuel_cost(arr):
    possible_positions = list(range(min(arr), max(arr) + 1))
    fuel_cost = float('inf')
    for pos in possible_positions:
        cost_to_pos = calc_fuel_cost(pos, arr)
        if cost_to_pos < fuel_cost:
            fuel_cost = cost_to_pos

    return fuel_cost


print(calc_least_fuel_cost(crabPositions))
