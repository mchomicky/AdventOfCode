import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/1/input',
                   headers={'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

# Split the raw data into a list, remove empty string
data = res.text.split('\n')
while '' in data:
    data.remove('')

# Function to count the number of increases in the data
def count_increases(arr, inc=0):
    for i in range(1, len(arr)):
        if int(arr[i]) > int(arr[i - 1]):
            inc += 1
    return inc


print(count_increases(data))
