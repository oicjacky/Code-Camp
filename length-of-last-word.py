''' 
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
 
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 
Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.


'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split(' ')[-1]
        return len(last_word)

    def lengthOfLastWord(self, s: str) -> int:
        count = start_count = 0
        for ele in s[::-1]:
            # skip space
            if ele != ' ':
                start_count = 1
            # counter
            if start_count and ele != ' ':
                count += 1
            # breaker
            if count > 0 and ele == ' ':
                break
        return count


if __name__ == '__main__':

    print(Solution().lengthOfLastWord('Hello World'))
    print(Solution().lengthOfLastWord('   fly me   to   the moon  '))
    print(Solution().lengthOfLastWord('luffy is still joyboy'))