from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arrayNumber = []
        node = head
        

        while(node != None):
            arrayNumber.append(node.val)
            node = node.next

        l =0 
        r = len(arrayNumber)-1

        while(l <= r):
            if(arrayNumber[l] != arrayNumber[r]):
                return False
            l = l +1
            r = r -1
        return True
        
        

ListNode4 = ListNode(1)
ListNode3 = ListNode(2, ListNode4)
ListNode2 = ListNode(2, ListNode3)
ListNode1 = ListNode(1, ListNode2)


obj = Solution()
print(obj.isPalindrome(ListNode1))
