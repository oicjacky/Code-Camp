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

    #NOTE: O(N + set of dict) (PR83 28 ms	14.3 MB)
    def wordPattern(self, pattern: str, s: str) -> bool:
        ''' Implement a 1-1 function between `pattern` and `s`.
        1. create a dictionary `pattern2s`
        2. Not one-to-one, means that it occurs the following situations:
            i. one `pattern` corresponds to two value in `s`
            ii. many `pattern` correspond to one value in `s`
        3. Not onto i.e. length of patterns not equals to length of words
        '''
        pattern2s = {}
        words = s.split(' ')
        if len(words) != len(pattern): 
            return False
        for p, word in zip(pattern, words):
            if p not in pattern2s:
                pattern2s[p] = word
            else:
                if pattern2s[p] != word:
                    print('[False]', pattern2s, 'occur value collision {', p, ':', word, '}')
                    return False
        if len(set(pattern2s.keys())) != len(set(pattern2s.values())):
            print('[False]', set(pattern2s.keys()), set(pattern2s.values()))
            return False
        print('[True]', pattern2s)
        return True

    #NOTE: more clear, more faster (PR95 24 ms	14.4 MB)
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''Use `set(zip(pattern, words))` to satisfy 2 above.'''
        words = s.split(' ')
        print(set(zip(pattern, words)))
        return len(pattern) == len(words) and \
                len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))


if __name__ == '__main__':

    print(Solution().wordPattern("abba", "dog cat cat dog")) #T
    print(Solution().wordPattern("abba", "dog cat cat fish")) #F
    print(Solution().wordPattern("abba", "dog dog dog dog")) #F many-to-one
    print(Solution().wordPattern("aaa", "aa aa aa aa")) #F
    print(Solution().wordPattern("aba", "dog cat cat")) #F