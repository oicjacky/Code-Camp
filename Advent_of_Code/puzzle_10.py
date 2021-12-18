''' Day 10: SYNTAX Scoring '''

TEST = False
INPUTS = 'puzzle_10.txt' if not TEST else 'puzzle_10_test.txt'
def read_puzzle_input():
    with open(INPUTS, 'r') as f:
        content = f.read().split('\n')
    return content
INPUTS_LINES = read_puzzle_input()

SYNTAX = {
    'open': ['(', '[', '{', '<'],
    'close': [')', ']', '}', '>'],
    'complete': ['()', '[]', r'{}', '<>'],
}

def delete_complete(s: str, complete: str):
    split_list = s.split(complete)
    while len(split_list) > 1:
        res = ''
        for ele in split_list:
            res += ele
        split_list = res.split(complete)
    return split_list[0]

def recursive_delete_complete(s: str):
    old_len = None
    while not old_len or old_len > len(s):
        old_len = len(s)
        for complete in SYNTAX['complete']:
            s = delete_complete(s, complete)
    return s
#NOTE:
# 0. Recursively delete the complete syntax.

def question_1():
    ''' For Corrupted ones '''
    SCORE = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    illegal = []
    for s in INPUTS_LINES:
        print('The string is', s)
        s = recursive_delete_complete(s)

        incorrect = []
        for i in range(len(s)):
            if s[i] in SYNTAX['close']:
                print('wrong close', s[i])
                incorrect.append(s[i])
                break
        if not incorrect:
            print('the string is just incomplete.')
        illegal += incorrect

    ans = 0
    for ele in illegal:
        ans += SCORE[ele]
    print('The ans is', ans)
    

def question_2():
    ''' For Imcomplete ones '''
    OPEN2CLOSE = {op : cl for op, cl in zip(SYNTAX['open'], SYNTAX['close'])}
    collect_scores = []
    for s in INPUTS_LINES:
        print('The string is', s)
        s = recursive_delete_complete(s)

        is_incomplete = [ s[i] not in SYNTAX['close'] for i in range(len(s))]
        if not all(is_incomplete):
            print('this is corrupted.')
            continue

        res = ''
        for ele in s[::-1]:
            res += OPEN2CLOSE[ele]

        incomplete_score = {')': 1, ']': 2, '}': 3, '>': 4}
        score = 0
        for ele in res:
            score *= 5
            score += incomplete_score[ele]
        collect_scores.append(score)
        print('scoring', score)
    
    collect_scores.sort()
    print('The middle score is' ,collect_scores[len(collect_scores)//2])
        

if __name__ == '__main__':

    question_1()
    question_2()