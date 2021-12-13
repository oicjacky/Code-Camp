''' Day 8: Seven Segment Search 
Reference
---------
[jack-mil's github](https://github.com/jack-mil/advent_of_code/blob/master/2021/8.py)
'''

TEST = True
INPUTS = 'puzzle_8.txt' if not TEST else 'puzzle_8_test.txt'

def read_puzzle_input(input):
    with open(input, 'r') as f:
        con = f.read().split('\n')
    return con
DIGITS = read_puzzle_input(INPUTS)
DIGITS_OUTPUT = list(map(lambda s: s.split(' | ')[1], DIGITS))

def question_1():
    '''Count digits 1 4 7 or 8 in output
    1: 2 segments
    4: 4 segments
    7: 3 segments
    8: 7 segments
    '''
    segments_1478 = [2, 4, 3, 7]
    digits_output_map = {}
    for output in DIGITS_OUTPUT:
        four_digit = output.split(' ')
        four_digit_length = list(map(lambda s: len(s), four_digit))
        digits_output_map[output] = four_digit_length
    # print(digits_output_map)

    ans = 0
    for val_list in digits_output_map.values():
        for val in val_list:
            if val in segments_1478:
                ans += 1
    print(f'The number of digits 1, 4, 7, 8 w.r.t {segments_1478} is {ans}.')
    

if __name__ == '__main__':
    
    print('Input digits', DIGITS, 'output', DIGITS_OUTPUT)
    question_1()

    decoder = {
        'acedgfb': 8,
        'cdfbe': 5,
        'gcdfa': 2,
        'fbcad': 3,
        'dab': 7,
        'cefabd': 9,
        'cdfgeb': 6,
        'eafb': 4,
        'cagedb': 0,
        'ab': 1
    }

    for output_str in DIGITS_OUTPUT:
        output_list = output_str.split()

        decoded = ''
        for val in output_list:
            for k, v in decoder.items():
                if set(val) == set(k):
                    print(val, k)
                    decoded += str(v)
        print(decoded)