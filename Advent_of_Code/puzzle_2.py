''' Day 2: Dive! '''

PLANNED_COURSE = ['forward 1', 'down 3', 'down 2', 'up 1', 'down 7', 'down 8', 'forward 6', 'forward 1', 'forward 1', 'down 6', 'up 3', 'down 7', 'down 1', 'down 6', 'forward 6', 'down 6', 'forward 3', 'up 7', 'forward 5', 'down 4', 'forward 6', 'forward 1', 'forward 6', 'forward 9', 'forward 3', 'up 1', 'forward 7', 'down 9', 'forward 2', 'up 9', 'down 5', 'down 3', 'up 1', 'down 6', 'down 7', 'down 8', 'down 7', 'forward 7', 'forward 3', 'down 5', 'down 2', 'forward 4', 'forward 7', 'down 8', 'down 4', 'down 5', 'down 1', 'forward 4', 'up 6', 'forward 6', 'forward 4', 'forward 5', 'up 3', 'up 6', 'down 4', 'down 8', 'forward 4', 'forward 5', 'down 3', 'forward 1', 'down 5', 'down 5', 'forward 8', 'forward 9', 'forward 1', 'forward 8', 'forward 5', 'forward 6', 'up 8', 'down 3', 'forward 8', 'up 2',
    'down 3', 'down 9', 'up 9', 'forward 5', 'down 2', 'forward 7', 'forward 5', 'forward 5', 'down 2', 'down 3', 'forward 7', 'forward 9', 'down 9', 'forward 3', 'forward 3', 'down 3', 'forward 3', 'up 6', 'down 4', 'forward 3', 'forward 3', 'forward 7', 'down 4', 'forward 8', 'up 8', 'down 3', 'down 2', 'forward 2', 'down 6', 'down 6', 'up 7', 'up 9', 'down 4', 'up 7', 'up 8', 'down 6', 'down 1', 'forward 6', 'forward 9', 'forward 1', 'forward 8', 'down 4', 'up 3', 'forward 6', 'down 5', 'forward 7', 'forward 5', 'down 2', 'forward 7', 'down 6', 'forward 7', 'up 2', 'up 5', 'forward 3', 'down 6', 'down 9', 'down 9', 'forward 9', 'up 7', 'down 6', 'down 4', 'down 8', 'forward 6', 'up 6', 'down 2', 'forward 5', 'up 7', 'forward 5', 'down 1', 'up 8', 'forward 2', 'forward 4', 'down 5',
    'down 8', 'up 7', 'up 5', 'down 2', 'forward 8', 'forward 4', 'up 6', 'forward 8', 'down 3', 'down 2', 'down 2', 'forward 4', 'forward 2', 'forward 9', 'up 3', 'up 7', 'up 3', 'up 5', 'forward 5', 'up 8', 'forward 3', 'forward 1', 'down 3', 'down 8', 'forward 6', 'forward 5', 'up 5', 'down 9', 'down 1', 'down 9', 'forward 9', 'up 3', 'forward 7', 'forward 6', 'forward 1', 'up 3', 'forward 9', 'forward 7', 'down 9', 'up 6', 'forward 2', 'up 9', 'forward 6', 'forward 4', 'up 3', 'forward 5', 'down 4', 'up 8', 'up 4', 'up 9', 'down 1', 'down 7', 'forward 7', 'forward 2', 'down 9', 'forward 7', 'forward 2', 'down 6', 'down 9', 'up 6', 'down 7', 'down 2', 'down 7', 'down 6', 'down 4', 'down 4', 'forward 6', 'forward 9', 'forward 4', 'down 7', 'down 5', 'up 6', 'down 7', 'forward 2',
    'down 3', 'down 1', 'forward 1', 'forward 5', 'down 4', 'down 4', 'down 1', 'down 9', 'forward 6', 'down 3', 'forward 5', 'up 7', 'forward 9', 'down 8', 'down 3', 'up 2', 'up 2', 'forward 4', 'down 7', 'forward 2', 'forward 5', 'forward 4', 'forward 3', 'down 8', 'down 6', 'forward 9', 'down 1', 'forward 1', 'down 1', 'up 8', 'down 2', 'forward 2', 'up 5', 'down 7', 'forward 8', 'down 7', 'down 4', 'forward 2', 'forward 6', 'up 2', 'forward 8', 'forward 2', 'forward 1', 'up 5', 'down 4', 'down 8', 'forward 4', 'down 8', 'up 8', 'forward 3', 'down 5', 'forward 2', 'forward 1', 'up 3', 'forward 9', 'up 5', 'forward 5', 'forward 5', 'up 8', 'down 6', 'forward 3', 'down 4', 'up 5', 'forward 3', 'up 6', 'forward 6', 'forward 9', 'down 7', 'down 7', 'down 8', 'down 4', 'forward 4',
    'forward 3', 'forward 3', 'forward 5', 'down 3', 'forward 8', 'up 5', 'forward 1', 'up 7', 'down 5', 'forward 7', 'forward 3', 'down 3', 'forward 2', 'forward 1', 'forward 4', 'up 2', 'down 8', 'forward 9', 'forward 9', 'down 6', 'down 1', 'down 5', 'forward 4', 'down 2', 'forward 1', 'up 7', 'down 9', 'forward 3', 'down 5', 'down 5', 'up 6', 'down 6', 'forward 8', 'down 1', 'up 3', 'down 2', 'up 1', 'forward 5', 'down 4', 'down 6', 'forward 8', 'down 4', 'down 5', 'down 2', 'forward 5', 'forward 8', 'down 8', 'up 4', 'forward 2', 'up 2', 'down 9', 'forward 6', 'forward 1', 'forward 5', 'up 2', 'down 1', 'up 7', 'up 3', 'forward 3', 'down 7', 'forward 2', 'forward 4', 'up 7', 'forward 4', 'forward 6', 'up 2', 'forward 4', 'forward 2', 'down 6', 'down 5', 'down 5', 'down 6',
    'forward 9', 'up 4', 'down 4', 'down 7', 'up 6', 'up 9', 'up 4', 'down 4', 'up 7', 'down 9', 'down 9', 'forward 3', 'down 7', 'down 7', 'down 7', 'down 2', 'up 2', 'up 1', 'up 6', 'down 8', 'up 7', 'down 4', 'forward 8', 'down 7', 'up 1', 'down 5', 'down 3', 'forward 6', 'up 1', 'down 5', 'forward 3', 'forward 6', 'forward 7', 'forward 2', 'down 3', 'forward 1', 'up 9', 'down 5', 'up 2', 'up 9', 'up 2', 'up 2', 'forward 1', 'down 2', 'forward 1', 'down 7', 'forward 1', 'forward 8', 'down 9', 'down 1', 'forward 9', 'forward 7', 'forward 7', 'down 5', 'down 5', 'down 3', 'forward 6', 'down 7', 'down 4', 'forward 2', 'up 6', 'down 3', 'up 4', 'up 7', 'forward 2', 'forward 8', 'forward 4', 'down 7', 'down 9', 'up 1', 'down 2', 'up 8', 'down 2', 'up 6', 'forward 6', 'up 5', 'down 2',
    'forward 5', 'down 4', 'forward 7', 'down 3', 'down 5', 'forward 1', 'down 7', 'forward 1', 'up 1', 'forward 4', 'up 4', 'forward 4', 'forward 5', 'forward 7', 'down 7', 'down 2', 'up 4', 'down 2', 'down 3', 'forward 3', 'forward 2', 'forward 5', 'forward 2', 'up 8', 'forward 3', 'down 7', 'down 9', 'forward 3', 'forward 6', 'down 7', 'down 5', 'down 3', 'up 3', 'forward 5', 'forward 2', 'down 1', 'up 1', 'up 8', 'down 6', 'down 4', 'down 1', 'forward 1', 'down 7', 'up 8', 'forward 2', 'forward 8', 'forward 8', 'forward 7', 'down 1', 'forward 8', 'down 8', 'forward 4', 'down 3', 'up 9', 'down 8', 'forward 9', 'down 7', 'up 2', 'forward 9', 'down 4', 'up 3', 'up 4', 'up 4', 'forward 5', 'up 2', 'forward 3', 'down 5', 'forward 5', 'down 5', 'up 8', 'down 4', 'forward 6', 'down 6',
    'forward 7', 'forward 2', 'down 2', 'up 7', 'down 5', 'down 9', 'down 8', 'down 4', 'up 3', 'forward 4', 'down 8', 'down 8', 'down 9', 'down 7', 'forward 2', 'forward 8', 'up 5', 'forward 8', 'down 9', 'forward 6', 'up 1', 'down 6', 'forward 1', 'up 4', 'down 3', 'forward 3', 'forward 2', 'down 6', 'forward 7', 'up 6', 'up 9', 'down 1', 'forward 3', 'forward 4', 'forward 2', 'up 8', 'forward 9', 'up 7', 'down 2', 'forward 2', 'up 7', 'down 2', 'up 6', 'down 2', 'forward 9', 'forward 3', 'down 6', 'down 5', 'down 3', 'forward 9', 'down 8', 'down 8', 'down 2', 'down 7', 'up 3', 'forward 1', 'down 7', 'up 8', 'up 8', 'forward 5', 'forward 5', 'forward 1', 'down 8', 'down 6', 'forward 2', 'up 3', 'forward 1', 'forward 7', 'forward 4', 'forward 5', 'forward 9', 'forward 7', 'forward 6',
    'forward 3', 'forward 4', 'down 8', 'down 1', 'forward 6', 'forward 9', 'forward 6', 'forward 9', 'forward 6', 'up 3', 'down 8', 'forward 4', 'forward 1', 'down 4', 'forward 9', 'down 8', 'down 3', 'up 2', 'forward 5', 'forward 2', 'forward 5', 'down 6', 'down 3', 'up 1', 'down 9', 'up 5', 'forward 6', 'down 7', 'forward 1', 'forward 9', 'down 2', 'down 5', 'forward 3', 'forward 6', 'down 4', 'down 5', 'up 4', 'forward 7', 'forward 5', 'down 8', 'forward 6', 'down 5', 'forward 2', 'down 7', 'forward 4', 'forward 8', 'down 8', 'forward 2', 'forward 8', 'down 5', 'forward 7', 'down 8', 'down 1', 'forward 8', 'down 4', 'up 4', 'down 7', 'down 6', 'up 5', 'forward 4', 'forward 1', 'forward 4', 'down 5', 'forward 5', 'forward 9', 'down 1', 'forward 3', 'up 7', 'down 1', 'down 7', 'forward 2',
    'down 5', 'down 6', 'forward 5', 'up 2', 'down 9', 'forward 1', 'up 5', 'forward 6', 'forward 9', 'forward 4', 'up 4', 'down 6', 'up 9', 'up 5', 'down 2', 'up 9', 'down 2', 'down 4', 'down 8', 'down 2', 'forward 2', 'forward 2', 'down 9', 'up 5', 'forward 2', 'forward 8', 'down 2', 'down 2', 'down 9', 'down 3', 'down 9', 'up 9', 'up 3', 'down 1', 'down 9', 'down 2', 'forward 7', 'down 2', 'up 3', 'down 9', 'up 2', 'up 4', 'forward 5', 'forward 7', 'down 7', 'up 7', 'up 5', 'down 8', 'up 2', 'forward 2', 'down 3', 'down 5', 'forward 2', 'forward 3', 'forward 3', 'down 1', 'down 1', 'forward 9', 'down 5', 'down 7', 'forward 7', 'forward 5', 'up 9', 'forward 3', 'up 4', 'forward 1', 'forward 3', 'down 4', 'forward 9', 'down 5', 'down 3', 'down 5', 'forward 6', 'down 6', 'forward 2', 'up 4',
    'down 4', 'forward 2', 'down 8', 'up 9', 'forward 9', 'forward 4', 'down 8', 'forward 2', 'forward 5', 'forward 1', 'forward 5', 'up 1', 'forward 7', 'forward 9', 'down 5', 'forward 6', 'down 1', 'forward 6', 'down 2', 'forward 9', 'down 1', 'forward 1', 'down 4', 'down 6', 'down 2', 'up 7', 'up 5', 'forward 8', 'forward 1', 'down 8', 'forward 1', 'forward 2', 'down 8', 'forward 7', 'down 5', 'forward 1', 'down 2', 'up 7', 'forward 7', 'down 4', 'down 8', 'up 6', 'up 4', 'forward 7', 'down 3', 'up 5', 'down 5', 'forward 7', 'up 7', 'down 6', 'forward 8', 'down 7', 'down 2', 'up 3', 'down 9', 'down 7', 'down 8', 'forward 4', 'forward 3', 'forward 9', 'forward 6', 'up 7', 'forward 5', 'down 4', 'down 5', 'forward 6', 'up 9', 'down 6', 'down 7', 'down 8', 'down 9', 'down 4', 'up 5', 'down 4',
    'forward 5', 'forward 3', 'down 3', 'down 7', 'up 8', 'forward 5', 'down 8', 'down 1', 'down 6', 'down 9', 'up 4', 'up 1', 'down 8', 'down 3', 'down 8', 'up 4', 'down 7', 'down 6', 'forward 7', 'up 9', 'down 4', 'down 1', 'down 6', 'down 2', 'forward 7', 'down 2', 'down 7', 'forward 3', 'forward 6', 'up 2', 'down 4', 'up 1', 'forward 4', 'up 2', 'down 4', 'up 3', 'down 8', 'up 9', 'forward 8', 'down 5', 'down 4', 'forward 8', 'down 1', 'down 8', 'forward 3', 'down 4', 'forward 5', 'down 5', 'up 9', 'forward 1', 'down 9', 'down 1', 'forward 4', 'forward 9', 'up 1', 'forward 4', 'forward 2', 'down 9', 'down 1', 'forward 1', 'down 2', 'forward 2', 'down 5', 'up 4', 'up 7', 'down 8', 'forward 3', 'up 1', 'down 4', 'forward 5', 'up 2', 'forward 4', 'forward 2', 'down 1', 'forward 4', 'forward 1',
    'up 5', 'forward 8', 'forward 4', 'forward 1', 'down 6', 'down 7', 'up 4', 'forward 9', 'up 6', 'forward 9', 'forward 3', 'forward 2', 'down 2', 'forward 7', 'up 7', 'forward 7', 'down 4', 'down 6', 'forward 8', 'up 8', 'forward 1', 'forward 3', 'forward 3', 'up 8', 'down 1', 'up 9', 'forward 1', 'up 1', 'down 7', 'forward 7', 'up 5', 'forward 5', 'up 9', 'up 3', 'forward 2', 'forward 6', 'up 1', 'forward 5', 'up 1', 'down 3', 'down 5', 'forward 8', 'up 5', 'forward 1', 'down 8', 'forward 4', 'down 3', 'down 1', 'down 7', 'forward 7', 'forward 3', 'down 4', 'forward 9', 'up 5', 'down 2', 'forward 4', 'up 7', 'up 5', 'forward 3', 'down 7', 'forward 8', 'up 4', 'up 2', 'forward 2', 'down 9', 'forward 4', 'down 5', 'forward 2', 'down 9', 'down 5', 'up 7', 'forward 3', 'down 8', 'forward 7', 'forward 9',
    'down 5', 'forward 2', 'forward 9', 'forward 5', 'down 5', 'up 4', 'down 6', 'down 6', 'forward 8', 'forward 5', 'forward 4', 'down 5', 'forward 2', 'down 8', 'forward 9', 'down 1', 'down 8', 'down 7', 'up 9', 'down 7', 'down 1', 'forward 7', 'forward 9', 'forward 8', 'up 2', 'forward 6', 'down 3', 'down 6', 'up 4', 'forward 4', 'forward 5', 'down 9', 'down 5', 'forward 1', 'down 2', 'forward 1', 'down 1', 'up 1', 'up 7', 'up 5', 'forward 6', 'forward 3'
]

def get_command_numbers():
    COMMAND2SIGN = {
        #NOTE command : ( horizontal=0; o.w. depth=1, sign of number )
        'forward': (0, True),
        'down': (1, True),
        'up': (1, False)
    }
    commands, numbers = [], []
    for ele in list(map(lambda s: s.split(' '), PLANNED_COURSE)):
        commands.append(COMMAND2SIGN[ele[0]])
        numbers.append(int(ele[1]))
    #print(commands, numbers)
    return commands, numbers

def question_1():
    ''' The submarine can take a series of commands as following,
    - forward X: increases the horizontal position by X units.
    - down X: increases the depth by X units.
    - up X: decreases the depth by X units.
    '''
    horizontal_0, depth_1 = 0, 0
    commands, numbers = get_command_numbers()
    for direction_sign, number in zip(commands, numbers):
        if direction_sign[0] == 1:
            if direction_sign[1]:
                depth_1 += number
            else:
                depth_1 -= number
        else:
            horizontal_0 += number
    print('Final position is (horizontal, depth) = (', horizontal_0, ', ', depth_1, ')')
    return horizontal_0* depth_1


def question_2():
    ''' In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0.
    - down X: increases your aim by X units.
    - up X: decreases your aim by X units.
    - forward X does two things:
        - It increases your horizontal position by X units.
        - It increases your depth by your aim multiplied by X.
    '''
    horizontal_0, aim, depth_1 = 0, 0, 0
    commands, numbers = get_command_numbers()
    for direction_sign, number in zip(commands, numbers):
        if direction_sign[0] == 1:
            if direction_sign[1]:
                aim += number
            else:
                aim -= number
        else:
            horizontal_0 += number
            depth_1 += aim*number
    print('Final position is (horizontal, depth) = (', horizontal_0, ', ', depth_1, ')')
    return horizontal_0* depth_1


if __name__ == '__main__':

    print(question_1())
    print(question_2())