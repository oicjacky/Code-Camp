''' 
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1

 
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
from typing import List

class Solution:

    #NOTE: use `collections.Counter`. very fast and light! (148 ms	15.4 MB)
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        return counter.most_common(1)[0][0]

    #NOTE: not bad! (152 ms	15.5 MB)
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for ele in nums:
            if ele not in nums_dict:
                nums_dict[ele] = 1
            else:
                nums_dict[ele] += 1
        nums_dict_reflection = {val : ele for ele, val in nums_dict.items()}
        print(nums_dict, nums_dict_reflection)
        return nums_dict_reflection[max(nums_dict.values())]
    
    #NOTE: replace `nums_dict` above with `collections.defaultdict` (164 ms	15.7 MB)
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        nums_dict = defaultdict(int)
        for ele in nums:
            nums_dict[ele] += 1
        nums_dict_reflection = {val : key for key, val in nums_dict.items()}
        return nums_dict_reflection[max(nums_dict.values())]


if __name__ == '__main__':

    print(Solution().majorityElement([3,2,3])) #3
    print(Solution().majorityElement([2,2,1,1,1,2,2])) #2
    print(Solution().majorityElement([0,0,1,1,3,4,0,0])) #0