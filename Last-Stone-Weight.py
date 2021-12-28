''' 
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.
 
Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

 
Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''
import heapq
from typing import List

class Solution:

    #NOTE: sorting list(queue) PR: 87, 55(28 ms	14.3 MB)
    #TODO: use O(n^2) insertion sort
    def lastStoneWeight(self, stones: List[int]) -> int: 
        while len(stones) > 1:
            print(stones)
            stones.sort()
            largest = stones.pop()
            second = stones.pop()
            stones.append(largest - second)
        return stones[0]

    #NOTE: use [Heap](https://docs.python.org/zh-tw/3/library/heapq.html) and heap sort O(n*logn)
    def lastStoneWeight(self, stones: List[int]) -> int:
        reversed_stones = [-ele for ele in stones]
        heapq.heapify(reversed_stones)
        while len(reversed_stones) > 1:
            print(reversed_stones)
            heapq.heappush(reversed_stones, heapq.heappop(reversed_stones) - heapq.heappop(reversed_stones))
        return -reversed_stones[0]


if __name__ == '__main__':

    print(Solution().lastStoneWeight([2,7,4,1,8,1])) #1
    print(Solution().lastStoneWeight([3])) #3
    print(Solution().lastStoneWeight([3,7,2])) #2
    print(Solution().lastStoneWeight([0,0,0])) #0