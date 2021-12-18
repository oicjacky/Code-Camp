''' Day 11: Dumbo Octopus '''
import numpy as np

TEST = False
INPUTS = 'puzzle_11.txt' if not TEST else 'puzzle_11_test.txt'
def read_puzzle_input():
    with open(INPUTS, 'r') as f:
        content = f.read().replace('\n', '')
    return np.array([ int(s) for s in content], dtype=np.int8).reshape(10, 10)
ENERGY = read_puzzle_input()
STEP = 100

def flash(pivot: tuple, mat: np.ndarray, flashed: set):
    ''' How a Octopus flashes that increases the energy level of all adjacent (including diagonal ones) octopuses by 1.
    up [i-1, j], down [i+1, j], left [i, j-1], right [i, j+1]
    leftup [i-1,j-1], rightup [i-1,j+1], leftdown [i+1, j-1], rightdown [i+1, j+1]'''
    row_operation = col_operation = [0, -1, 1]
    for i in range(3):
        for j in range(3):
            _row = pivot[0] + row_operation[i]
            _col = pivot[1] + col_operation[j]
            if _row >= mat.shape[0] or _row < 0 or \
                _col >= mat.shape[1] or _col < 0:
                continue
            if _row == pivot[0] and _col == pivot[1]:
                mat[_row, _col] = 0
            else:
                mat[_row, _col] += 1
            if (_row, _col) in flashed:
                mat[_row, _col] = 0
    return mat
#NOTE: Testing `flash`
#ENERGY = np.array([ int(s) for s in '1111119991191911999111111'], dtype=np.int8).reshape(5, 5)
#flash((0, 0), ENERGY)

def question_1(ENERGY):
    number_of_flash = 0
    for step in range(1, STEP + 1):
        print('This is step', step)
        ENERGY += 1
        flashed_octopus = set()
        old_energy = np.empty_like(ENERGY, dtype=np.int8)
        while (old_energy != ENERGY).any():
            old_energy = ENERGY.copy()
            for row in range(ENERGY.shape[0]):
                for col in range(ENERGY.shape[1]):
                    if ENERGY[row, col] > 9:
                        flashed_octopus.add((row, col))
                        ENERGY = flash((row, col), ENERGY, flashed_octopus)
        
        number_of_flash += len(flashed_octopus)
        del old_energy, flashed_octopus
        print(ENERGY)
    print(f'After {STEP} there have been a total of {number_of_flash} flashes.')

def question_2(ENERGY):
    step = 0
    while (ENERGY != 0).any():
        print('This is step', step)
        step += 1
        ENERGY += 1
        flashed_octopus = set()
        old_energy = np.empty_like(ENERGY, dtype=np.int8)
        while (old_energy != ENERGY).any():
            old_energy = ENERGY.copy()
            for row in range(ENERGY.shape[0]):
                for col in range(ENERGY.shape[1]):
                    if ENERGY[row, col] > 9:
                        flashed_octopus.add((row, col))
                        ENERGY = flash((row, col), ENERGY, flashed_octopus)
    print('The first step which all octopuses flash is', step)


if __name__ == '__main__':

    question_1(ENERGY.copy())
    question_2(ENERGY.copy())