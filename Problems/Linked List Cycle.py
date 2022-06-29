
from lib2to3.pytree import Node
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        firstNode = head

        if(firstNode == None ):
            return False

        secondNode = head.next

        while(firstNode != None and secondNode != None):
            if(firstNode == secondNode):
                return True

            firstNode = firstNode.next
            
            if(secondNode != None and secondNode.next != None):
                secondNode = secondNode.next.next
            else:
                return False
        
        return False

# Node4 = ListNode(-4)
# Node3 = ListNode(0)
# Node2 = ListNode(2)
# Node1 = ListNode(3)


# Node1.next = Node2
# Node2.next = Node3
# Node3.next=  Node4
# Node4.next= Node2

Node2 = ListNode(2)
Node1 = ListNode(3)


Node1.next = Node2

obj = Solution()
print(obj.hasCycle(Node1))
