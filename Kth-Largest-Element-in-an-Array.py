''' 
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

 
Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
'''
import heapq
from typing import List

class Solution:
    # [heap sort and list sort](https://stackoverflow.com/questions/24666602/python-heapq-vs-sorted-complexity-and-performance)
    #NOTE: use heap (56 ms	15.3 MB)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [ -ele for ele in nums ]
        heapq.heapify(heap)
        return -heapq.nsmallest(k, heap)[-1]

    #NOTE: use list.sort() (52 ms	15.1 MB)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], 2)) #5
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)) #4