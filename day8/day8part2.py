import requests

# Request the input for the challenge, cookie header from inspecting browser request while logged in
res = requests.get('https://adventofcode.com/2021/day/8/input',
                   headers={
                       'cookie': 'session=53616c7465645f5f19185ed23d15808085c52371d52fbe5627bf39757b9a8072118b68a52d2134e8a2ff229bedd45dce'})

data = res.text.strip()

# Nested list comprehension returns 3D array where each array item contains an array for the signal and an array for the outputs
data = [[signal_output.split() for signal_output in entry.split(' | ')] for entry in data.strip().split('\n')]


# Find all the digits that have a unique number of segments and return a dict with the segment letters used for each digit
def find_unique_digits(arr):
    digits = {}
    for output in arr[0]:
        if len(output) == 2:
            digits['1'] = output
        elif len(output) == 4:
            digits['4'] = output
        elif len(output) == 3:
            digits['7'] = output
        elif len(output) == 7:
            digits['8'] = output

    return digits


# Find digits with 6 segments. From inspecting common segments between these and the unique digits, we can see:
# 9 is the only 6 segment digit that contains the same segments as 4
# 0 doesn't contain the same segments as 4, but does have the same segments as 7
# 6 doesn't contain the same segments as 4 or 7
def find_6_segment_digits(arr, key_dict):
    digits = {}
    for output in arr[0]:
        # Only interested in digits we haven't found yet and that are 6 letters long
        if output in key_dict or len(output) != 6:
            continue
        if list(filter(lambda x: x in output, list(key_dict['4']))) == list(key_dict['4']):
            digits['9'] = output
        elif list(filter(lambda x: x in output, list(key_dict['7']))) == list(key_dict['7']):
            digits['0'] = output
        else:
            digits['6'] = output

    return digits | key_dict


# Find digits with 6 segments. From inspecting common segments between these and the unique digits, we can see:
# 3 is the only 5 segment digit that contains the same segments as 7
# 5 doesn't contain the same segments as 7, but all segments of 5 are contained by 6
# 2 doesn't contain the same segments as 7, and the segments of 2 are not contained by 6
def find_5_segment_digits(arr, key_dict):
    digits = {}
    for output in arr[0]:
        # Only interested in digits we haven't found yet and that are 6 letters long
        if output in key_dict or len(output) != 5:
            continue
        if list(filter(lambda x: x in output, list(key_dict['7']))) == list(key_dict['7']):
            digits['3'] = output
        elif list(filter(lambda x: x in key_dict['6'], list(output))) == list(output):
            digits['5'] = output
        else:
            digits['2'] = output

    return digits | key_dict


def decode_output(arr, key_dict):
    # Swap the keys and values of our key dict so each output digit can be easily looked up
    # Sort the new keys in alphabetic order since the outputs aren't necessarily in the same order as the signal pattern
    key = {''.join(sorted(v)): k for k, v in key_dict.items()}
    output = ''
    for digit in arr[1]:
        output += key[''.join(sorted(digit))]

    return int(output)


def calc_result(arr):
    result = 0
    for signal_output in arr:
        # Solve each set of segments, adding to the pattern key as we go; sum up the output value for each signal/output
        pattern_key = find_unique_digits(signal_output)
        pattern_key = find_6_segment_digits(signal_output, pattern_key)
        pattern_key = find_5_segment_digits(signal_output, pattern_key)
        result += decode_output(signal_output, pattern_key)

    return result


print(calc_result(data))
