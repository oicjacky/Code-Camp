''' 
Given the root of a binary tree, invert the tree, and return its root.
 
Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
import sys
sys.path.append(r'C:\Users\user\Pyvirtualenv\code_test')

from utils import TreeNode, Generator
from typing import Optional

class Solution:

    #NOTE: Wrong, it should return a inverted `TreeNode`
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        invert = [root.val]
        queue = [(root.left, root.right)]
        while queue:
            left_node, right_node = queue.pop(0) #FIFO
            if not right_node:
                continue
            else:
                invert.append(right_node.val)            
                queue.append((right_node.left, right_node.right))
            if not left_node:
                continue
            else:
                invert.append(left_node.val)
                queue.append((left_node.left, left_node.right))
        return invert

    #NOTE: O(n) For each node, change the left subtree and right subtree. PR: 67, 76 (32 ms	14.2 MB)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root


if __name__ == '__main__':

    print(Solution().invertTree(Generator.generate_tree([4,2,7,1,3,6,9])))
    print(Solution().invertTree(Generator.generate_tree([2,1,3])))
    print(Solution().invertTree(Generator.generate_tree([])))