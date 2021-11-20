''' 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
from typing import List

class Solution:

    #NOTE: O(n^2) try all combinations of the two numbers in `nums` (4156 ms	15 MB)
    def twoSum_On2(self, nums: List[int], target: int) -> List[int]:
        for idx_a in range(len(nums)):
            for idx_b in range(idx_a+1, len(nums)):
                if (nums[idx_a] + nums[idx_b]) == target:
                    return idx_a, idx_b

    #NOTE: memory usage PR:98 (4664 ms	14.6 MB)
    def twoSum_On2_memory(self, nums: List[int], target: int) -> List[int]:
        return [[idx_a, idx_b] for idx_a in range(len(nums)) for idx_b in range(idx_a+1, len(nums)) if (nums[idx_a] + nums[idx_b]) == target][0]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        canditates = [ (index, val, val - target) for index, val in enumerate(nums) if val - target <= 0 ]
        for idx_a in range(len(canditates)):
            for idx_b in range(len(nums)):
                if canditates[idx_a][0] == idx_b:
                    continue
                print(canditates[idx_a][2], nums[idx_b])
                if (canditates[idx_a][2] + nums[idx_b]) == 0:
                    return canditates[idx_a][0], idx_b
            

        

if __name__ == '__main__':

    print(Solution().twoSum([2, 7, 5, 11], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))
    print(Solution().twoSum([-3, 4, 3, 90], 0))
    print(Solution().twoSum([-1,-2,-3,-4,-5], -8))