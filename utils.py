class ListNode:
    ''' Definition for singly-linked list. '''
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next} }}"

class TreeNode:
    '''Definition for a binary tree node.'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return "TreeNode{{ val= {0}, left= {1}, right= {2} }}".format(
            self.val, self.left, self.right)


class Generator:

    @staticmethod
    def generate_listnode(input_list: list, pos: int) -> ListNode:
        if not input_list:
            return ListNode(None)
        list_nodes = [ ListNode(ele) for ele in input_list]
        for index in range(len(list_nodes)-1):
            if not list_nodes[index].next:
                list_nodes[index].next = list_nodes[index+1]
        if pos >= 0:
            list_nodes[-1].next = list_nodes[pos]
        else:
            list_nodes[-1].next = None
        return list_nodes[0]

    @staticmethod
    def generate_tree(tree_inputs: list) -> TreeNode:
        tree_nodes = [ TreeNode(ele) for ele in tree_inputs]
        counter_id = 1
        for node in tree_nodes:
            if not node.left:
                if counter_id >= len(tree_nodes): break
                node.left = tree_nodes[counter_id] if tree_nodes[counter_id].val else None
                counter_id += 1
            if not node.right:
                if counter_id >= len(tree_nodes): break
                node.right = tree_nodes[counter_id] if tree_nodes[counter_id].val else None
                counter_id += 1
        return tree_nodes[0]
