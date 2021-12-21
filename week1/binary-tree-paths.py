''' 
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
 
Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

 
Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''
import sys
sys.path.append(r'C:\Users\user\Pyvirtualenv\code_test')

from utils import TreeNode, Generator
from typing import Optional, List

class Solution:

    #NOTE: stardard solution
    # For each node, there are 2 condition:
    #    i. a leaf, no children
    #    ii. not leaf, has children
    # For example, [1, 2, 3, None, 5]
    # -1: self.binaryTreePaths on '1' left and right
    # -1.left:  self.binaryTreePaths on '2' left and right
    # -1.left-2.left: null!
    # -1.left-2.right: 5 no children.
    # -1.right: 3 no children.
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            print(root, ', a null.')
            return []
        if not root.left and not root.right:
            print(root.val, 'has no children.')
            return [str(root.val)]
        print(root.val, 'has children, finding left and right.')
        results = sum(map(self.binaryTreePaths, (root.left, root.right)), [])
        results = [str(root.val) + '->' + substr for substr in results]
        print('results', results)
        return results

if __name__ == '__main__':

    root = Generator.generate_tree([1, 2, 3, None, 5])
    print(root)
    
    print(Solution().binaryTreePaths(Generator.generate_tree([1, 2, 3, None, 5])))
    print(Solution().binaryTreePaths(Generator.generate_tree([1])))