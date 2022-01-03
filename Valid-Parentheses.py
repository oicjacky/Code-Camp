''' 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

 
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    
    #NOTE: very slow (52 ms	14.4 MB)
    def isValid(self, s: str) -> bool:
        SYNTAX = {
            'complete' : ['()', '[]', r'{}'],
        }
        def delete_complete(s: str, complete: str):
            split_list = s.split(complete)
            while len(split_list) > 1:
                res = ''
                for ele in split_list:
                    res += ele
                split_list = res.split(complete)
            return split_list[0]
        
        def recursive_delete_complete(s: str):
            old_len = len(s) +1
            while old_len > len(s):
                old_len = len(s)
                for complete in SYNTAX['complete']:
                    s = delete_complete(s, complete)
            return s
        return True if not recursive_delete_complete(s) else False

    #NOTE: use stack (32 ms	14.3 MB)
    def isValid(self, s: str) -> bool:
        SYNTAX = {
            #'open': ['(', '[', '{'],
            'closed': [')', ']', '}'],
            'complete' : ['()', '[]', r'{}'],
        }
        stack = []
        for ele in s:
            if ele in SYNTAX['closed'] and stack:
                paste = stack[-1] + ele
                if paste in SYNTAX['complete']:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        print(stack)
        return True if not stack else False


if __name__ == '__main__':

    print(Solution().isValid('()')) #T
    print(Solution().isValid(r'()[]{}')) #T
    print(Solution().isValid(r'(]')) #F
    print(Solution().isValid(r'([]{})')) #T
    print(Solution().isValid(r'([{]})')) #F
    print(Solution().isValid(r']')) #F
    print(Solution().isValid(r'](')) #F