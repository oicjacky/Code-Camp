''' 
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
 
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
from typing import List

class Solution:

    #NOTE: O(n^2) this raises Time Executed Limit!
    def maxSubArray_all_combination(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for l in range(1, len(nums)-i+1):
                res.append(sum(nums[i:(i+l)]))
                print(i, i+l, nums[i:(i+l)])
        print(len(res))
        return max(res)

    #NOTE: a reversed version of above one
    def maxSubArray_all_combination_reversed(self, nums: List[int]) -> int:
        res = []
        const = len(nums)
        for i in range(len(nums)):
            for l in range(1, len(nums)-i+1):
                res.append(sum(nums[(const-i-l):const-i]))
                print(const - i, const - i-l, nums[(const-i-l):const-i], sum(nums[(const-i-l):const-i]))
        print(len(res))
        return max(res)

    #NOTE: O(n^2) this try to skip the unnecessary part of `nums`
    def _maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)-1):
            if nums[i] < 0 and nums[i+1] > 0: 
                continue
            for l in range(1, len(nums)-i+1):    
                s = sum(nums[i:(i+l)])
                if s > res:
                    res = s
                print(i, i+l, nums[i:(i+l)])
        if nums[-1] > res:
            res = nums[-1]
            print(res, nums[-1])
        return res

    def maxSubArray(self, nums: List[int]) -> int:
        '''This is the O(n) algorithm for finding maximum subarray.
        
        Algorithm:
            1. Given index i in {0, ..., len(nums)-1}, find the maximum subarray from `nums[0]` to `nums[i]`.
                if nums[i] > (nums[0] + ... + nums[i-1] + nums[i]):
                    max_subarr_i = nums[i]
                else:
                    max_subarr_i = (nums[0] + ... + nums[i-1] + nums[i])
            2. Keep the maximum summed number when upating `max_subarr_i`.
        '''
        max_num = max_subarr_i = nums[0]
        print('i = ', 0, 'val = ', nums[0], 'max subarray_i = ', max_subarr_i, 'max num', max_num)
        for i in range(1, len(nums)):
            max_subarr_i = max(max_subarr_i+nums[i], nums[i])
            max_num = max(max_subarr_i, max_num)
            print('i = ', i, 'val = ', nums[i], 'max subarray_i = ', max_subarr_i, 'max num', max_num)
        return max_num


if __name__ == '__main__':

    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print('\n')
    print(Solution().maxSubArray([5,4,-1,7,8]))
    print('\n')
    print(Solution().maxSubArray([1]))
    print('\n')
    print(Solution().maxSubArray([-2,-1,5]))
    print('\n')
    print(Solution().maxSubArray([-1,2,3]))
    print('\n')