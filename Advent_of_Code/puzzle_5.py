''' Day 5: Hydrothermal Venture '''
import numpy as np

TEST = False
INPUTS = 'puzzle_5.txt' if not TEST else 'puzzle_5_test.txt'
def read_puzzle_inputs():
    vents_records = {
        'from': {
            'column': [], 'row': [] },
        'end': {
            'column': [], 'row': [] }
    }
    with open(INPUTS, 'r') as f:
        con = f.read().split('\n')
        res = list(map(lambda ele: ele.split(' -> '), con))
        for ele in res:
            from_, end_ = ele[0].split(','), ele[1].split(',')
            vents_records['from']['column'].append(int(from_[0]))
            vents_records['from']['row'].append(int(from_[1]))
            vents_records['end']['column'].append(int(end_[0]))
            vents_records['end']['row'].append(int(end_[1]))
    print(vents_records)
    return vents_records

def vents_diagram(vents_records):
    max_num = max(vents_records['from']['column'] + vents_records['from']['row'] + \
        vents_records['end']['column'] + vents_records['end']['row'])
    min_num = min(vents_records['from']['column'] + vents_records['from']['row'] + \
        vents_records['end']['column'] + vents_records['end']['row'])
    size = len(list(range(max_num+1)))
    diagram_mat = np.zeros((size,size), dtype=int)
    print(max_num, min_num, diagram_mat)
    for from_col, from_row, end_col, end_row in zip(vents_records['from']['column'], vents_records['from']['row'], vents_records['end']['column'], vents_records['end']['row']):
        print(from_row, from_col, '->', end_row, end_col)
        if from_row == end_row:
            print('Cond_1: equal row')
            min_col, max_col = min(from_col, end_col), max(from_col, end_col)
            diagram_mat[from_row, min_col:max_col+1] += 1
        elif from_col == end_col:
            print('Cond_2: equal column')
            min_row, max_row = min(from_row, end_row), max(from_row, end_row)
            diagram_mat[min_row:max_row+1, from_col] += 1
        elif from_row == from_col and end_row == end_col:
            print('Cond_3: diagonal')
            min_, max_ = min(from_row, end_row), max(from_col, end_col)
            di = tuple(map(lambda di: di[min_:max_+1] ,
                            np.diag_indices_from(diagram_mat)))
            diagram_mat[di] += 1
        elif from_row == end_col and from_col == end_row:
            print('Cond_4: anti-diagonal')
            min_, max_ = min(from_row, end_row), max(from_col, end_col)
            di = list(map(lambda di: di[min_:max_+1] ,
                            np.diag_indices_from(diagram_mat)))
            di[0] = di[0][::-1]
            diagram_mat[tuple(di)] += 1
        elif np.abs((from_col-end_col) / (from_row-end_row)) == 1:
            print('Cond_5: 45-degree diagonal lines')
            row_direction, col_direction = 1 if from_row < end_row else -1, 1 if from_col < end_col else -1
            row_range = range(from_row, end_row+1 if row_direction==1 else end_row-1, row_direction)
            col_range = range(from_col, end_col+1 if col_direction==1 else end_col-1, col_direction)
            row_arr = np.array([], dtype=int)
            col_arr = np.array([], dtype=int)
            for ele in zip(row_range, col_range):
                row_arr = np.append(row_arr, ele[0])
                col_arr = np.append(col_arr, ele[1])
            # print('dia', tuple(zip(row_range, col_range)))
            # print((row_arr, col_arr))
            diagram_mat[(row_arr, col_arr)] += 1
        #print(diagram_mat)
    return diagram_mat


if __name__ == '__main__':

    vents_records = read_puzzle_inputs()
    diagram_mat = vents_diagram(vents_records)

    print('The number of points >= 2 is', (diagram_mat >= 2).sum())