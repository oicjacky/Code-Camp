''' 
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
 
Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 231 - 1
'''
# The isBadVersion API is already defined for you.
class Solution:
    
    def __init__(self, bad) -> None:
        self.bad = bad

    def isBadVersion(self, version: int) -> bool:
        return True if version >= self.bad else False

    #NOTE: Time Limit Exceeded
    def firstBadVersion(self, n: int) -> int:
        for ver in range(1, n+1):
            if self.isBadVersion(ver):
                return ver
    
    #NOTE: use binary search
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while right - left > 1:
            mid = (left + right) //2
            print(mid, (left, right))
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid
        print('Now left and right are neighborhood', (left, right))
        return left if self.isBadVersion(left) else right


if __name__ == "__main__":
    
    print(Solution(bad = 4).firstBadVersion(n = 5))
    print(Solution(bad = 1).firstBadVersion(n = 1))
    print(Solution(bad = 1702766719).firstBadVersion(n = 2126753390))