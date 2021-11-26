''' 
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
 
Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true

 
Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''
class Solution:

    #NOTE: Fail, this does not preserve the order of occurance isomorphic
    def _isIsomorphic(self, s: str, t: str) -> bool:
        s_set, t_set = set(s), set(t)
        s2t_tbl = { k:v for k, v in zip(s_set, t_set) }
        print(s2t_tbl)
        if len(s_set) != len(t_set):
            return False

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        s2t_tbl = {}
        # since constraints: t.length == s.length
        ans = ''
        for ele_s, ele_t in zip(s, t):
            if s2t_tbl.get(ele_s) == None:
                s2t_tbl.update({ele_s : ele_t})
            ans += s2t_tbl[ele_s] 
        print(s2t_tbl, ans, t)
        return ans == t




if __name__ == '__main__':

    print(Solution().isIsomorphic('egg', 'add'))
    print(Solution().isIsomorphic('foo', 'bar'))
    print(Solution().isIsomorphic('paper', 'title'))
    print(Solution().isIsomorphic('bbbaaaba', 'aaabbbba')) #False
    print(Solution().isIsomorphic('badc', 'baba')) #False