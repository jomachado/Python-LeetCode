# Definition for singly-linked list.
from multiprocessing.sharedctypes import Value
from platform import node
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution: 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListCustom(head, None)

    def reverseListCustom(self, head: Optional[ListNode], previousHead: Optional[ListNode]) -> Optional[ListNode]:
        if(head.next == None or head == None):
            return head

        returnValue = self.reverseListCustom(head.next, head)
        head.next.next =  head
        head.next = None
        return returnValue
        
            




obj = Solution()


node4 = ListNode(4, None )

teste2 = obj.reverseList(node4)
teste1= teste2


        