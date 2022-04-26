''' 
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.
 
Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

 
Constraints:
1 <= n <= 231 - 1
1 <= pick <= n
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
class Solution:

    def __init__(self, pick) -> None:
        self.pick = pick

    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0

    #NOTE: use binary search
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while right - left > 1:
            mid = (left + right) //2
            print(mid, (left, right))
            if self.guess(mid) > 0:
                left = mid
            else:
                right = mid
        print('Now left and right are neighborhood', (left, right))
        return left if self.guess(left) == 0 else right


if __name__ == "__main__":
    
    print(Solution(pick = 6).guessNumber(n = 10))
    print(Solution(pick = 1).guessNumber(n = 1))
    print(Solution(pick = 1).guessNumber(n = 2))