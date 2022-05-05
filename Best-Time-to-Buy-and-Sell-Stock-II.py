''' 
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
 
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

 
Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''
from typing import List

class Solution:

    #NOTE: Add if-condition to `maxProfit` of best-time-to-buy-and-sell-stock-I.py
    # If earn_so_far greater than 0, then sell
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        earn_so_far = 0
        min_so_far = prices[0]
        for i in range(1, len(prices)):
            earn_so_far = max(prices[i] - min_so_far, earn_so_far)
            min_so_far = min(min_so_far, prices[i])
            print(f'[day {i+1}]', prices[i], min_so_far, earn_so_far)
            if earn_so_far > 0:
                print('get', earn_so_far)
                profit += earn_so_far
                earn_so_far = 0
                min_so_far = prices[i] #buy it immediately
        return profit
    
    #NOTE: Greedy collect all positive profit
    def maxProfit(self, prices: List[int]) -> int:
        return sum(curr - prev for prev, curr in zip(prices, prices[1:]) if curr - prev > 0)

if __name__ == '__main__':

    print(Solution().maxProfit([7,1,5,3,6,4])) #4+3
    print(Solution().maxProfit([1,2,3,4,5])) #4
    print(Solution().maxProfit([7,6,4,3,1])) #0
    print(Solution().maxProfit([6,1,3,2,4,7])) #2+2+3