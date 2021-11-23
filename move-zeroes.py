''' 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]

 
Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

 
Follow up: Could you minimize the total number of operations done?
'''
from typing import List

class Solution:

    #NOTE: Time Limit Exceeded
    def moveZeroes(self, nums: List[int]) -> None:
        times = len([ele for ele in nums if ele == 0])
        for time in range(times):
            for i in range(len(nums)-time-1):
                if nums[i] == 0:
                    # change i and i+1
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                print(nums)

    #NOTE: O(n). Move the non-zeros to the front of `nums`, hence the remainders will be all zeros!
    def moveZeroes(self, nums: List[int]) -> None:
        i = count = 0
        while i < len(nums):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[count]
                nums[count] = temp
                count += 1
            i += 1
            print(nums)
            

if __name__ == '__main__':

    print(Solution().moveZeroes([0,1,-10,3,12]))
    print(Solution().moveZeroes([0,1,0,3,12]))
    print(Solution().moveZeroes([0]))