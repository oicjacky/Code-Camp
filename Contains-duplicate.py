''' 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
from typing import List

class Solution:

    #NOTE: (124 ms	21.5 MB)
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        1. create a dictionary `nums_dict` with (key, value) = (element of nums, the number of occurring element)
        2. return False if all value in `nums_dict` equals to 1; otherwise, return True.
        '''
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        print(nums_dict)
        if all([ val == 1 for val in nums_dict.values()]):
            return False
        else:
            return True

    #NOTE: O(sort) use sort (128 ms	18.7 MB) 
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any([nums[i] - nums[i+1] == 0 for i in range(len(nums)-1)])

    #NOTE: use built-in `set` (120 ms	20 MB)
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == '__main__':

    print(Solution().containsDuplicate([1,2,3,1])) #T
    print(Solution().containsDuplicate([1,2,3,4])) #F
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])) #T