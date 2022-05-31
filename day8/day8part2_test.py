data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

data = [[signal_output.split() for signal_output in entry.split(' | ')] for entry in data.strip().split('\n')]

sampleData = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

sampleData = [[signal_output.split() for signal_output in entry.split(' | ')] for entry in sampleData.strip().split('\n')]


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


def find_6_segment_digits(arr, key_dict):
    digits = {}
    for output in arr[0]:
        if output in key_dict or len(output) != 6:
            continue
        if list(filter(lambda x: x in output, list(key_dict['4']))) == list(key_dict['4']):
            digits['9'] = output
        elif list(filter(lambda x: x in output, list(key_dict['7']))) == list(key_dict['7']):
            digits['0'] = output
        else:
            digits['6'] = output

    return digits | key_dict


def find_5_segment_digits(arr, key_dict):
    digits = {}
    for output in arr[0]:
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
    key = {''.join(sorted(v)): k for k, v in key_dict.items()}
    output = ''
    for digit in arr[1]:
        output += key[''.join(sorted(digit))]

    return int(output)


def calc_result(arr):
    result = 0
    for signal_output in arr:
        pattern_key = find_unique_digits(signal_output)

        pattern_key = find_6_segment_digits(signal_output, pattern_key)

        pattern_key = find_5_segment_digits(signal_output, pattern_key)

        result += decode_output(signal_output, pattern_key)

    return result


print(calc_result(data))
