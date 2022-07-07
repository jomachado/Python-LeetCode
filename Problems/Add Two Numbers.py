from typing import Optional
from unittest import result

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbersCustom(self, l1: Optional[ListNode], l2: Optional[ListNode], carry) -> Optional[ListNode]:
        if(l1 == None and l2 == None):
            if(carry > 0):
                return ListNode(carry, None)
            else:
                return None

        firstValue = l1.val if l1 != None else 0
        secondValue = l2.val if l2 != None else 0

        addValue = (firstValue + secondValue)+carry
        resultValue = addValue % 10
        newcarry = int(addValue/10)

        resultListNode = ListNode(resultValue, None)
        resultListNode.next = self.addTwoNumbersCustom(l1.next if l1 != None else None , l2.next if l2 != None else None, newcarry)
        return resultListNode        

   
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersCustom(l1, l2, 0)        

