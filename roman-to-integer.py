''' 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
 
Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 
Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].


'''
class Solution:
    
    D = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }
    
    #NOTE: first submissions, runtime = 68 ms and memory = 14.4 MB
    def split(self, s, idx:list) -> list:
        pair = [ (i , j) for i, j in zip([0] + idx, idx + [len(s)])]
        res = []
        for st, ed in pair:
            res.append(s[st:ed])
        return res
    
    def romanToInt_0(self, s: str) -> int:
        s_list = [ Solution.D[ele] for ele in s ]
        s_list_rev = s_list[::-1]
        coll_idx = []
        for idx, (front, back) in enumerate(zip(s_list_rev, s_list_rev[1:])):
            if front <= back:
                #split and 
                coll_idx.append(idx+1)
            else:
                pass
        splited_list = self.split(s_list_rev, coll_idx)
        res = 0
        for ele in splited_list:
            if len(ele) > 1:
                res += (ele[0] - ele[1])
            else:
                res += ele[0]
        return res

    #NOTE: second submissions, runtime = 44 ms and memory = 14.4 MB
    def romanToInt_1(self, s: str) -> int:
        '''A reversed version that calculate the roman from back to front'''
        s_list = [ Solution.D[ele] for ele in s[::-1] ]
        ans = 0
        counter = 0
        for i in range(len(s_list)):
            if counter > 0:
                ans -= s_list[i]
            else:
                ans += s_list[i]
            if i < len(s_list)-1 and s_list[i] > s_list[i+1]:
                counter += 1
            else:
                counter = 0
        return ans

    #NOTE: third submissions, runtime = 36 ms and memory = 14.4 MB
    def romanToInt(self, s: str) -> int:
        '''A formal version that calculate the roman from front to end'''
        s_list = [ Solution.D[ele] for ele in s ]
        ans = 0
        for i in range(len(s_list)):
            if i < len(s_list)-1 and s_list[i] < s_list[i+1]:
                ans -= s_list[i]
            else:
                ans += s_list[i]
        return ans

if __name__ == '__main__':

    print(Solution().romanToInt('III'))
    print(Solution().romanToInt('LVIII'))
    print(Solution().romanToInt('MCMXCIV'))
    print(Solution().romanToInt('CMXII'))