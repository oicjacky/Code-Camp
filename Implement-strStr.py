''' 
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
 
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:
Input: haystack = "", needle = ""
Output: 0

 
Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.


'''
class Solution:

    #NOTE: use `re` (96 ms	19.3 MB)
    def _strStr_re_search(self, haystack: str, needle: str) -> int:
        import re
        res = re.search(needle, haystack)
        return res.start() if res is not None else -1

    #NOTE: use built-in `in` (32 ms	14.3 MB)
    def _strStr_in(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            if len(haystack) == 0 or len(needle) == 0:
                return 0
            else:
                return haystack.index(needle)
        else:
            return -1
    
    #NOTE: slicing by index (60 ms	14.5 MB)
    def strStr(self, haystack: str, needle: str) -> int:
        offset = len(needle)
        if offset == 0:
            return 0
        for idx in range(len(haystack)-offset+1):
            if needle == haystack[idx:(idx+offset)]:
                #print('stop at',idx)
                return idx
        return -1


if __name__ == '__main__':

    print(Solution().strStr('hello', 'll')) #2
    print(Solution().strStr('aaaaa', 'bba')) #-1
    print(Solution().strStr('', '')) #0
    print(Solution().strStr('a', '')) #0
    print(Solution().strStr('', 'a')) #-1
    print(Solution().strStr('a', 'aa')) #-1
    print(Solution().strStr('bbbbb', 'a')) #-1
    print(Solution().strStr('mississippi', 'issip')) #4