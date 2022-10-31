''' 
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
 
Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
Example 3:
Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.

 
Constraints:
1 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
'''
from typing import List

class Solution:
    
    #NOTE: First, find the largest. Then check all elements except largest.
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        largest = max(nums)
        idx = nums.index(largest)
        nums.pop(idx)
        for ele in nums:
            if ele*2 > largest:
                return -1
        return idx

    #NOTE: Greedy get largest and second largest number and only need to check 2 * second
    def dominantIndex(self, nums: List[int]) -> int:
        largest_so_far = 0
        second_largest = 0
        ans = 0
        for idx, ele in enumerate(nums):
            if ele > largest_so_far:
                largest_so_far, second_largest = ele, largest_so_far
                ans = idx
            elif ele > second_largest:
                second_largest = ele
        return ans if largest_so_far >= 2* second_largest else -1



if __name__ == "__main__":
    print(Solution().dominantIndex([3,6,1,0]))
    print(Solution().dominantIndex([1,2,3,4]))
    print(Solution().dominantIndex([1]))