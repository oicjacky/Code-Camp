''' 
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

 
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
import sys
sys.path.append(r'C:\Users\user\Pyvirtualenv\code_test')

from utils import TreeNode, Generator
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def Depth(root):
            if not root:
                return 0
            left = Depth(root.left)
            right = Depth(root.right)
            if abs(left - right) > 1:
                raise Exception('The depth of subtree is greater than two!')
            return max([left, right]) +1
        try:
            Depth(root)
        except Exception as error:
            print(error)
            return False
        else:
            return True
        
    

if __name__ == '__main__':
    
    print(Solution().isBalanced(Generator.generate_tree([3,9,20,None,None,15,7]))) #T
    print(Solution().isBalanced(Generator.generate_tree([1,2,2,3,3,None,None,4,4]))) #F
    print(Solution().isBalanced(Generator.generate_tree([1,2,2,3,None,None,3,4,None,None,4]))) #F