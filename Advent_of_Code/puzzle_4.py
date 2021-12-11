''' Day 4: Giant Squid '''
import re
import numpy as np

TEST = False
INPUTS = 'puzzle_4.txt' if not TEST else 'puzzle_4_test.txt'
def read_puzzle_inputs():
    with open(INPUTS, 'r') as f:
        inputs = f.read().split('\n\n')
        bingo_numbers = inputs[0]
        boards_list = inputs[1:]
    print(type(bingo_numbers), type(boards_list))
    return bingo_numbers, boards_list

BINGO, BOARDS = read_puzzle_inputs()

if __name__ == '__main__':
    
    print(BINGO, [ ele for ele in BOARDS[-3:]])

    #THOUGHT:
    # 1. Create the boards:
    # (board_index, values, marked_bool)
    # can use `dict` or `numpy.array`
    # 2. Start the bingo game:
    # in each round, check if anyone is winner which 
    # has at least one complete row or column of marked numbers.
    # if someone wins, the game is over; otherwise, continue.
    def make_the_boards() -> dict:         
        '''board_index :  { values , marked_bool }'''
        global bingo_size
        bingo_size = 5
        the_boards = { index : {'values': [], 'marked': []} \
            for index in range(len(BOARDS)) }
        
        for index, val in enumerate(BOARDS):
            the_boards[index]['values'] = np.array([ int(ele) for ele in re.split(r'[\\n\s]', val) if ele]).reshape(bingo_size, bingo_size)
            the_boards[index]['marked'] = np.array([ False for ele in range(bingo_size**2)]).reshape(bingo_size, bingo_size)
            ## use 'list'
            # for i in range(bingo_size):
            #     the_boards[index]['values'].append(values[bingo_size*i:bingo_size*(i+1)])
            #     the_boards[index]['marked'].append(marked[bingo_size*i:bingo_size*(i+1)])

        def check_length_bingo(ele):
            if not all([ len(ele) == bingo_size]):
                raise ValueError("The length bingo size is not correct!")
        for val in the_boards.values():
            check_length_bingo(val['values'])
            [check_length_bingo(ele) for ele in val['values'] ]
        return the_boards
    boards = make_the_boards()
    bingo = list(map(lambda ele: int(ele), BINGO.strip().split(',')))
    print(boards, bingo)
    
    
    def playing(question:int):
        winners_list = None if question == 1 else [False for i in range(len(boards))]
        for number in bingo:
            print("Round", number)
            for index, board in boards.items():
                marked_position = board['values'] == number
                if marked_position.any():
                    board['marked'][marked_position] = True

                if (board['marked'].sum(axis=0) == bingo_size).any() or \
                    (board['marked'].sum(axis=1) == bingo_size).any():
                    if question == 1:
                        print(f'The {index} wins!')
                        return index, number
                    elif question == 2:
                        winners_list[index] = True
                        if all(winners_list):
                            return index, number
        return None
    winner, number = playing(question=1)
    values = boards[winner]['values']
    markeds = boards[winner]['marked']
    ans = values[~markeds]
    print('the number', number, ', corresponding array', ans)
    print('The answer is', sum(ans.ravel())* number)
    
    winner, number = playing(question=2)
    values = boards[winner]['values']
    markeds = boards[winner]['marked']
    ans = values[~markeds]
    print('the number', number, ', corresponding array', ans)
    print('The answer is', sum(ans.ravel())* number)
    import pdb; pdb.set_trace()