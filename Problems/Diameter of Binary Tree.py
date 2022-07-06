# Definition for a binary tree node.


from ast import Nonlocal
from turtle import left
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def diameterOfBinaryTreeSub(root):
            nonlocal maxDiameter       

            if(root == None):
                return -1            
            
            left = diameterOfBinaryTreeSub(root.left)
            right = diameterOfBinaryTreeSub(root.right)


            diameter = left+right+2
            maxDiameter = max(maxDiameter, diameter)
            
            heightNode = max(left, right)+1


            return heightNode

        diameterOfBinaryTreeSub(root)     
        return maxDiameter   

#node6 = TreeNode(6)
node4 = TreeNode(4)
node5 = TreeNode(5)
#node5 = TreeNode(5, node6)

node2 = TreeNode(2, node4, node5)

node3 = TreeNode(3)

node1 = TreeNode(1,node2, node3)

obj = Solution()
print(obj.diameterOfBinaryTree(node1))