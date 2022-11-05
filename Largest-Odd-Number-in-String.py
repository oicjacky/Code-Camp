''' 
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.
 
Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

 
Constraints:
1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.
'''
class Solution:

    #NOTE: forward
    def largestOddNumber(self, num: str) -> str:
        if int(num) % 2 == 1:
            return num
        ans = ''
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                ans = num[:i+1]
        return ans

    #NOTE: backward. more fast!
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ''


if __name__ == "__main__":
    print(Solution().largestOddNumber("52"))
    print(Solution().largestOddNumber("4206"))
    print(Solution().largestOddNumber("35427"))
    print(Solution().largestOddNumber("35322"))