''' 
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 
Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
from typing import List

class Solution:
    
    #NOTE: Time Limit Exceeded
    def search(self, nums: List[int], target: int) -> int:
        temp = nums
        left = len(temp) //2
        while temp and target != temp[left]:
            # print(temp[left])
            if target < temp[left]:
                temp = temp[:left]
            elif target >= temp[left]:
                temp = temp[left:]
            left = len(temp) //2
            # print(temp)
        if temp:
            return nums.index(target)
        else:
            return False

    #NOTE: O(logN)
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while right - left > 1:
            mid = (left + right) //2
            print(nums[mid], (left, right))
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid
        print('Now left and right are neighborhood', (left, right))
        if target == nums[right]:
            return right
        elif target == nums[left]:
            return left
        else:
            return -1


if __name__ == "__main__":

    print(Solution().search([-1,0,3,5,9,12], 0)) #1
    print(Solution().search([-1,0,3,5,9,12], -2)) #-1
    print(Solution().search([-1,0,3,5,9,12], 1)) #-1
    print(Solution().search(list(range(100)), 1))
