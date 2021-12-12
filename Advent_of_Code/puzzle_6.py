''' Day 6: Lanternfish '''

TEST = False
INITIAL_STATE = [3, 4, 3, 1, 2] if TEST else \
    [4,1,4,1,3,3,1,4,3,3,2,1,1,3,5,1,3,5,2,5,1,5,5,1,3,2,5,3,1,3,4,2,3,2,3,3,2,1,5,4,1,1,1,2,1,4,4,4,2,1,2,1,5,1,5,1,2,1,4,4,5,3,3,4,1,4,4,2,1,4,4,3,5,2,5,4,1,5,1,1,1,4,5,3,4,3,4,2,2,2,2,4,5,3,5,2,4,2,3,4,1,4,4,1,4,5,3,4,2,2,2,4,3,3,3,3,4,2,1,2,5,5,3,2,3,5,5,5,4,4,5,5,4,3,4,1,5,1,3,4,4,1,3,1,3,1,1,2,4,5,3,1,2,4,3,3,5,4,4,5,4,1,3,1,1,4,4,4,4,3,4,3,1,4,5,1,2,4,3,5,1,1,2,1,1,5,4,2,1,5,4,5,2,4,4,1,5,2,2,5,3,3,2,3,1,5,5,5,4,3,1,1,5,1,4,5,2,1,3,1,2,4,4,1,1,2,5,3,1,5,2,4,5,1,2,3,1,2,2,1,2,2,1,4,1,3,4,2,1,1,5,4,1,5,4,4,3,1,3,3,1,1,3,3,4,2,3,4,2,3,1,4,1,5,3,1,1,5,3,2,3,5,1,3,1,1,3,5,1,5,1,1,3,1,1,1,1,3,3,1]

DAY = 80

def question_1():
    for day in range(DAY):
        print('Day', day)
        for fish_id in range(len(INITIAL_STATE)):
            if INITIAL_STATE[fish_id] == 0:
                INITIAL_STATE[fish_id] = 6
                INITIAL_STATE.append(8)
            else:
                INITIAL_STATE[fish_id] -= 1
        # print(INITIAL_STATE)
    print(f'After {DAY} days, a total of {len(INITIAL_STATE)} fish.')


def question_1_numpy():
    import numpy as np
    initial_state = np.array(INITIAL_STATE, dtype=np.int8)

    for day in range(1, DAY+1):
        print('Day', day)
        is_zero = initial_state == 0
        initial_state[~is_zero] -= 1
        if is_zero.any():
            number_of_new_fish = np.sum(is_zero)
            new_fishes = np.array([ 8 for i in range(number_of_new_fish) ], dtype=np.int8)
            initial_state[is_zero] = 6
            initial_state = np.append(initial_state, new_fishes)
        # print(initial_state)
    print(f'After {DAY} days, a total of {len(initial_state)} fish.')


def question_2():
    ''' Use hash table of lanternfish that store the number of fishes in the corresponding age. '''
    from collections import defaultdict
    lanternfish = defaultdict(int)
    for ele in INITIAL_STATE:
        if ele not in lanternfish:
            lanternfish[ele] = 1
        else:
            lanternfish[ele] += 1
    print(lanternfish, '\n', [ k for k, v in lanternfish.items() for it in range(v)])
    
    for day in range(1, DAY+1):
        print('Day', day)
        for key, val in lanternfish.copy().items():
            # new fish
            if key == 0:
                lanternfish[6] += val
                lanternfish[8] += val
                lanternfish[0] -= val
            # minus 1
            else:
                lanternfish[key] -= val
                lanternfish[key-1] += val
        # print(lanternfish, '\n', [ k for k, v in lanternfish.items() for it in range(v)])
    ans = 0
    for val in lanternfish.values():
        ans += val
    print('ans', ans, 'lanternfish', lanternfish)


if __name__ == '__main__':

    # question_1()
    # question_1_numpy()
    question_2()