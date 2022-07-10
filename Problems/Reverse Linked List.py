from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution: 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListCustom(head, None)

    def reverseListCustom(self, head: Optional[ListNode], previousHead: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head

        returnValue = self.reverseListCustom(head.next, head)
        head.next.next =  head
        head.next = None
        return returnValue
        
            


        