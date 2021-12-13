''' Day 9: Smoke Basin '''
import numpy as np

TEST = False
INPUTS = 'puzzle_9.txt' if not TEST else 'puzzle_9_test.txt'

def read_puzzle_input():
    with open(INPUTS, 'r') as f:
        content = f.read().split('\n')
    return np.array(list(map(lambda line: [ele for ele in line], content)), dtype=np.int8)
HEIGHTMAP = read_puzzle_input()

def question_1():
    # THOUGHT:
    # for each element in matrix,
    # pass through the smaller height direction
    # until the position is the smallest one.

    lowest = {
        'point' : [],
        'up_low_left_right': []
    }
    rows, cols = HEIGHTMAP.shape
    for row in range(rows):
        for col in range(cols):
            print(f'({row}, {col}) = {HEIGHTMAP[row, col]}')

            # increment of up, down, left, right
            up_incre, down_incre, left_incre, right_incre = None, None, None, None
            up_row = row - 1
            if up_row >= 0:
                up_incre = HEIGHTMAP[row, col] - HEIGHTMAP[up_row, col]
            down_row = row + 1
            if down_row < rows:
                down_incre = HEIGHTMAP[row, col] - HEIGHTMAP[down_row, col]
            left_col = col - 1
            if left_col >= 0:
                left_incre = HEIGHTMAP[row, col] - HEIGHTMAP[row, left_col]
            right_col = col + 1
            if right_col < cols:
                right_incre = HEIGHTMAP[row, col] - HEIGHTMAP[row, right_col]
            # print(up_incre, down_incre, left_incre, right_incre)

            updownleftright = up_incre, down_incre, left_incre, right_incre
            if all([ ele < 0 for ele in updownleftright if ele is not None ]):
                lowest['point'].append((row, col))
                lowest['up_low_left_right'].append(updownleftright)
    ans = 0
    for p in lowest['point']:
        ans += (HEIGHTMAP[p]+1)
        # print(HEIGHTMAP[p]+1)
    print('The sum of risk levels is', ans)
    return lowest

def question_2(lowest):

    def get_horizontal_points(start_row_col:tuple, area_points):
        row, col = start_row_col
        # right
        next_col = col + 1
        while next_col < HEIGHTMAP.shape[1] and HEIGHTMAP[row, next_col] != 9:
            area_points.add((row, next_col)) #HEIGHTMAP[row, next_col]
            next_col += 1
        # left
        next_col = col - 1
        while next_col >= 0 and HEIGHTMAP[row, next_col] != 9:
            area_points.add((row, next_col)) #HEIGHTMAP[row, next_col]
            next_col -= 1
        return area_points

    def get_vertical_points(start_row_col:tuple, area_points):
        row, col = start_row_col
        # down
        next_row = row + 1
        while next_row < HEIGHTMAP.shape[0] and HEIGHTMAP[next_row, col] != 9:
            area_points.add((next_row, col)) #HEIGHTMAP[next_row, col]
            next_row += 1
        # up
        next_row = row - 1
        while next_row >= 0 and HEIGHTMAP[next_row, col] != 9:
            area_points.add((next_row, col)) #HEIGHTMAP[next_row, col]
            next_row -= 1
        return area_points
    
    
    area = {}
    for ele in lowest['point']:
        area_points = { ele }
        # left and right
        for ele in area_points.copy():
            #print(ele, area_points)
            area_points = get_horizontal_points(ele, area_points)

        # up and down
        for ele in area_points.copy():
            #print(ele, area_points)
            area_points = get_vertical_points(ele, area_points)

        # check all points in `area_points` that some points is ignored or not.
        new_number_points = None
        while not new_number_points or number_points < new_number_points:
            number_points = len(area_points)
            print(number_points, new_number_points)
            for ele in area_points.copy():
                #print(ele, area_points)
                area_points = get_horizontal_points(ele, area_points)
                area_points = get_vertical_points(ele, area_points)
            new_number_points = len(area_points)

        area[ele] = area_points

    # ans
    ans = 1
    length_of_area = list(map(lambda ele: len(ele), area.values()))
    for idx, ele in enumerate(sorted(length_of_area, reverse=True)):
        print('Area index', idx, ', length:', ele) 
        if idx < 3:
            ans *= ele
    print('The multiply of the three largest number is', ans)


if __name__ == '__main__':
    
    lowest = question_1()
    question_2(lowest)