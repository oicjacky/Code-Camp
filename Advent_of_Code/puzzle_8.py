''' Day 8: Seven Segment Search 
Reference
---------
    `questuin_1` in [jack-mil's github](https://github.com/jack-mil/advent_of_code/blob/master/2021/8.py)
'''
TEST = False
INPUTS = 'puzzle_8.txt' if not TEST else 'puzzle_8_test.txt'

def read_puzzle_input(input):
    with open(input, 'r') as f:
        con = f.read().split('\n')
    return con
DIGITS = read_puzzle_input(INPUTS)
DIGITS_OUTPUT = list(map(lambda s: s.split(' | ')[1], DIGITS))
DIGITS_INPUT = list(map(lambda s: s.split(' | ')[0].split(), DIGITS))

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
    
def decoder(length2input: dict) -> dict:
    ''' By inference of input digits with the known unique ones, (1, 4, 7, 8),
    we get the the mapping between signal wires and segments called `decoder`.

    Reference
    ---------
    My friend Sam's advise and inspiration in 'Advent_of_Code/puzzle_8_part2.png'
    '''
    # 1 + len_5 -> 3
    three = None
    for ele in length2input[5]:
        if all([ e in ele for e in length2input[2][0] ]):
            three = ele
            length2input[5].remove(ele)
    
    # 3 + len_6 -> 9
    nine = None
    for ele in length2input[6]:
        if all([ e in ele for e in three ]):
            nine = ele
            length2input[6].remove(ele)

    # 1 + len_6 -> 0 -> 6
    zero = six = None
    for ele in length2input[6]:
        if all([ e in ele for e in length2input[2][0] ]):
            zero = ele
            length2input[6].remove(ele)
    six = length2input[6][0]
    length2input[6].remove(six)

    # 9 + len_5 -> 5 -> 2
    five = two = None
    for ele in length2input[5]:
        if all([ e in nine for e in ele ]):
            five = ele
            length2input[5].remove(ele)
    two = length2input[5][0]
    length2input[5].remove(two)

    one = length2input[2][0]
    four = length2input[4][0]
    seven = length2input[3][0]
    eight = length2input[7][0]
    #print(length2input, three, nine, zero, six, five, two)
    decoded = { tuple(sorted(ele)) : idx \
        for idx, ele in enumerate([zero, one, two, three, four, five, six, seven, eight, nine]) }
    return decoded

def question_2():
    ''' Use `decoder` generating deoced mapping configuration 
    to solve the output digits.
    '''
    decoded_output = []
    for index, (input ,output) in enumerate(zip(DIGITS_INPUT, DIGITS_OUTPUT)):
        print('index', index)
        length2input = {}
        for ele in input:
            l = len(ele)
            if l not in length2input:
                length2input[l] = [ele]
            else:
                length2input[l] += [ele]
        decoded = decoder(length2input)

        four_digit = output.split(' ')
        decode_digit = ''
        for ele in four_digit:
            decode_digit += str(decoded[tuple(sorted(ele))])
        decoded_output.append(int(decode_digit))
    print('The answer is', sum(decoded_output))


if __name__ == '__main__':
    
    print('Input digits', DIGITS[:10])
    question_1()
    question_2()