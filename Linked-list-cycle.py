''' 
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
 
Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 
Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

 
Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''
from typing import Optional

class ListNode:
    ''' Definition for singly-linked list. '''
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f"ListNode{{val: {self.val}, next: {self.next} }}"

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
    
class Solution:

    #NOTE: +7's first answer, use a list to store `ListNode` and check if it has duplicated members. memory: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        runner = head
        cycle_list = []
        while runner not in cycle_list:
            if not runner:
                return False
            print(runner.val)
            cycle_list.append(runner)
            runner = runner.next
        return True

    #NOTE: only change list to dict from above. memory: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        runner = head
        cycle_map = {}
        while runner not in cycle_map:
            if not runner:
                return False
            print(runner.val)
            cycle_map[runner] = 1
            runner = runner.next
        return True

    #NOTE: +7's great thoughts, Two runner! memory: O(1)
    def hasCycle(self, head: ListNode) -> bool:        
        fast = slow = head
        while (fast and fast.next):
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False


if __name__ == '__main__':

    print(Solution().hasCycle(generate_listnode([3,2,0,-4], 1))) #T
    print(Solution().hasCycle(generate_listnode([1,2], 0))) #T
    print(Solution().hasCycle(generate_listnode([1], -1))) #F
    print(Solution().hasCycle(generate_listnode([1,2], -1))) #F
    print(Solution().hasCycle(generate_listnode([], -1))) #F