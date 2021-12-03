''' 
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
 
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", s = "dog dog dog dog"
Output: false

 
Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patter2s = {}
        words = s.split(' ')
        if len(words) != len(pattern): return False
        for p, word in zip(pattern, words):
            if p not in patter2s:
                patter2s[p] = word
            else:
                if patter2s[p] != word:
                    print(patter2s, 'occur value collision', word)
                    return False
        # prevent many-to-one
        if len(set(patter2s.keys())) != len(set(patter2s.values())):
            print(set(patter2s.keys()), set(patter2s.values()))
            return False
        print(patter2s)
        return True



if __name__ == '__main__':

    print(Solution().wordPattern("abba", "dog cat cat dog")) #T
    print(Solution().wordPattern("abba", "dog cat cat fish")) #F
    print(Solution().wordPattern("abba", "dog dog dog dog")) #many-to-one
    print(Solution().wordPattern("aaa", "aa aa aa aa")) #F