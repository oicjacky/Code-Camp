''' 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''
class Solution:

    def isAnagram_wrongAns(self, s: str, t: str) -> bool:
        return set(t) == set(s) and len(s) == len(t)

    #NOTE: use `collections.Counter`
    def isAnagram_Counter(self, s: str, t: str) -> bool:
        from collections import Counter
        print(Counter(s), Counter(t))
        return Counter(s) == Counter(t)

    #NOTE: O(N+M) with dictionary, not using `collections.Counter`
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for ele in s:
            if ele not in mapping_s:
                mapping_s[ele] = 0
            mapping_s[ele] += 1
        for ele in t:
            if ele not in mapping_t:
                mapping_t[ele] = 0
            mapping_t[ele] += 1    
        print(mapping_s, mapping_t)
        return mapping_s == mapping_t
        

if __name__ == '__main__':

    print(Solution().isAnagram('anagram', 'nagaram')) #T
    print(Solution().isAnagram('rat', 'car')) #F
    print(Solution().isAnagram('aa', 'a')) #F
    print(Solution().isAnagram('aacc', 'ccac')) #F