import numpy as np
from typing import Tuple

TEST = False
INPUTS = 'puzzle_13.txt' if not TEST else 'puzzle_13_test.txt'
def read_puzzle_input() -> Tuple[list]:
    with open(INPUTS, 'r') as f:
        content = f.read()
        points, fold = content.split('\n\n')
        points = list(map(lambda ele: tuple(ele.split(',')), points.split('\n')))
    return np.array(points, dtype=np.int16), fold.split('\n')

def make_fold_instructions(fold):
    fold_instructions = {
        'axis': [],
        'at': []
    }
    for ele in fold:
        axis, at = ele.split('=')
        fold_instructions['axis'].append(1 if axis[-1] == 'y' else 0)
        fold_instructions['at'].append(int(at))
    return fold_instructions

def get_coordinate_mask(points):
    left_top, right_buttom = np.min(points, axis=0), np.max(points, axis=0)
    rows, cols = points[:,0] , points[:,1]
    coordinate_mask = np.zeros(shape=(right_buttom[0]+1, right_buttom[1]+1), dtype=bool)
    coordinate_mask[rows, cols] = True
    return coordinate_mask

def folding(coordinate_mask, points, at, axis):
    ''' Update the points and coordinate_mask with folding operation (in-place).
    In coordinate, 
        (new + old)/2 = at
    i.e.
        new = 2*at - old
    '''
    col = 1 if axis else 0
    cond = points[:,col] > at
    coordinate_mask[points[cond,0], points[cond,1]] = False
    
    points[cond,col] = 2*at - points[cond,col]
    coordinate_mask[points[cond,0], points[cond,1]] = True
    return coordinate_mask, points


if __name__ == '__main__':

    points, fold = read_puzzle_input()
    fold_instructions = make_fold_instructions(fold)
    coordinate_mask = get_coordinate_mask(points)

    for i in range(len(fold)):
        print(f'fold along {fold_instructions["axis"][i]}={fold_instructions["at"][i]}, calculating distance...')
        folding(coordinate_mask, points,
                at=fold_instructions['at'][i],
                axis=fold_instructions['axis'][i])
        if i == 0:
           print(f'[Question 1] the first folding results in {np.sum(coordinate_mask)} dots') 
    print(f'after folding {np.sum(coordinate_mask)} dots are visible.')

    ans = ''
    for row in get_coordinate_mask(points).T:
        for col in row:
            ans += '#' if col else '.'
        ans += '\n'
    print(ans)