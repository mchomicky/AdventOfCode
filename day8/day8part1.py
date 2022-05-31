import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/8/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

data = [[signal_output.split() for signal_output in entry.split(' | ')] for entry in data.strip().split('\n')]

def count_easy_digits(arr):
    count = 0
    for signal_output in arr:
        count += len(list(filter(lambda x: len(x) in [2, 3, 4, 7], signal_output[1])))

    return count


easy_digits = count_easy_digits(data)
print(easy_digits)