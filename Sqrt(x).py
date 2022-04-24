'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:
0 <= x <= 231 - 1
'''
class Solution:

    #NOTE: Time Limit Exceeded
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for num in range(1, x+1):
            if num**2 == x:
                return num
            elif num**2 > x:
                return num -1

    #NOTE: Using binary search to reduce the search space.
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while right - left > 1:
            mid = (left + right) //2
            print(mid**2, (left, mid, right))
            if x < mid**2:
                right = mid
            elif x > mid**2:
                left = mid
            else:
                return mid
        print('Now left and right are neighborhood', (left, right))
        return left


if __name__ == "__main__":
    print(Solution().mySqrt(4)) #2
    print(Solution().mySqrt(8)) #2
    print(Solution().mySqrt(25)) #5
    print(Solution().mySqrt(180636561)) #13440