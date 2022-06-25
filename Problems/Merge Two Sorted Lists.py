#Definition for singly-linked list.
from ast import Return
from curses import noecho
from dbm import dumb
from http.client import NotConnected
from lib2to3.pytree import Node
from locale import currency
from optparse import Option
from this import d
from typing import List


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My first solution using While        
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         l1 = list1 
#         l2 = list2


#         currency = ListNode()
#         dumb = currency
#         while(l1 != None or l2 != None):
#             if(l1 == None):
#                 currency.next = l2
#                 l2 = l2.next
#             elif (l2 == None):
#                 currency.next = l1
#                 l1 = l1.next
#             else:
#                 if(l1.val < l2.val):
#                     currency.next = l1
#                     l1 = l1.next
#                 else:
#                     currency.next = l2
#                     l2 = l2.next
#             currency = currency.next    
#         return dumb.next

# My Second solution using recursive method
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2 
        elif (list2 == None):
            return list1            
        else:
            if(list1.val < list2.val):
                list1.next = self.mergeTwoLists(list1.next, list2)                                
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)            
                return list2
                

