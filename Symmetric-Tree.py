''' 
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
 
Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 
Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?
'''
import sys
sys.path.append(r'C:\Users\user\Pyvirtualenv\code_test')

from utils import TreeNode, Generator
from typing import Optional

class Solution:
    
    #NOTE: use 'binary tree path' to list all paths and check it is
    # symmetric or not.
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        def visit(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            # print(root.val, 'has children, finding left and right by', visit.__name__)
            left = visit(root.left)
            right = visit(root.right)
            left_path = [str(root.val) + ',L' + ele for ele in left]
            right_path = [str(root.val) + ',R' + ele for ele in right]
            return left_path + right_path
        all_paths = visit(root)
        # print('all paths is', all_paths)
        symmetric_counter = {}
        for p in all_paths:
            if p not in symmetric_counter:
                new_p = ''
                for ele in p.split(','):
                    if 'L' in ele:
                        new_p += ',' + ele.replace('L', 'R')
                    elif 'R' in ele:
                        new_p += ',' + ele.replace('R', 'L')
                    else:
                        new_p += ele
                symmetric_counter[new_p] = 1
            else:
                symmetric_counter[p] += 1
        # print(symmetric_counter)
        if all([ val%2 == 0 for val in symmetric_counter.values()]):
            return True
        return False
    
    #NOTE: a better way, faster and less memory.
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_symmetric(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 or not node2:
                #print('not node1 or not node2: NoneNone or NoneTreeNode')
                return node1 is node2
            #print('under', node1.val, node2.val)
            return node1.val == node2.val and \
                   is_symmetric(node1.left, node2.right) and \
                   is_symmetric(node1.right, node2.left)
        return is_symmetric(root.left, root.right)

    #NOTE: stack, a LIFO queue
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 or not node2:
                if node1 is not node2:
                    print('None & TreeNode')
                    return False
                else:
                    continue
            if node1.val != node2.val:
                return False
            print('adding left & ritht of node1 and node2', node1.val, node2.val)
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        return True


if __name__ == '__main__':

    print(Solution().isSymmetric(Generator.generate_tree([1,2,2,3,4,4,3]))) #T
    print(Solution().isSymmetric(Generator.generate_tree([1,2,2,None,3,None,3]))) #F
    print(Solution().isSymmetric(Generator.generate_tree([1,2]))) #F
    print(Solution().isSymmetric(Generator.generate_tree([1]))) #T