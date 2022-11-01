''' 
You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.
Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.
Note that abs(x) equals x if x >= 0, and -x otherwise.
 
Example 1:
Input: nums = [1,-1,1], limit = 3, goal = -4
Output: 2
Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.

Example 2:
Input: nums = [1,-10,9,1], limit = 100, goal = 0
Output: 1

 
Constraints:
1 <= nums.length <= 105
1 <= limit <= 106
-limit <= nums[i] <= limit
-109 <= goal <= 109
'''
from typing import List

class Solution:
    #NOTE: Time Limit Exceeded.
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        now = sum(nums)
        diff = abs(goal - now)
        ans = 0
        while diff > limit:
            diff = diff - limit 
            ans += 1
        ans += 1
        return ans

    #NOTE: Greedy to divide the difference
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        now = sum(nums)
        diff = abs(goal - now)
        times, mod = divmod(diff, limit)
        return times+1 if mod else times

if __name__ == "__main__":
    print(Solution().minElements([1,-1,1], 3, -4))
    print(Solution().minElements([1,-10,9,1], 100, 0))
    print(Solution().minElements([2,5,5,-7,4], 7, 464680098))
    