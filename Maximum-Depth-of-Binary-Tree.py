''' 
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

 
Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
import sys
sys.path.append(r'C:\Users\user\Pyvirtualenv\code_test')

from utils import TreeNode, Generator
from typing import Optional

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1
        def go(root, count):
            if not root:
                print('a null')
                return count-1
            if not root.left and not root.right:
                print(root.val, 'no children')
                return count
            print(root.val, 'go finding left and right, count +1')
            to_go = count + 1

            left_count = go(root.left, to_go)
            print('under', root.val, 'left is', left_count)
            right_count = go(root.right, to_go)
            print('under', root.val, 'right is', right_count)
            return max([left_count, right_count])
        res = go(root, count)
        return res

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        print(root.val, 'go finding left and right by', self.maxDepth.__name__)
        left = self.maxDepth(root.left)
        print('under', root.val, 'left is', left)
        right = self.maxDepth(root.right)
        print('under', root.val, 'right is', right)
        return max([left, right]) + 1

if __name__ == '__main__':

    print(Solution().maxDepth(Generator.generate_tree([3,9,20,None,None,15,7]))) #3
    print(Solution().maxDepth(Generator.generate_tree([1,None,2,None]))) #2
    print(Solution().maxDepth(Generator.generate_tree([5])))  #1
    print(Solution().maxDepth(Generator.generate_tree([1,2,3,4,None,None,5]))) #3    