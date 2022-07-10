from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricCustom(root.left, root.right)       

    def isSymmetricCustom(self, firstNode: Optional[TreeNode], secondNode: Optional[TreeNode]):
        if(firstNode == None and secondNode == None):
            return True

        if(firstNode == None or secondNode == None):
            return False;

        if(firstNode.val != secondNode.val):
            return False

        return self.isSymmetricCustom(firstNode.left, secondNode.right) and self.isSymmetricCustom(firstNode.right, secondNode.left)

        

firstTreeNode3 = TreeNode(3,None, None)
secondTreeNode3 = TreeNode(3,None, None)


firstTreeNode2 = TreeNode(2,firstTreeNode3, None)
secondTreeNode2 = TreeNode(2,None, secondTreeNode3)

firstTreeNode1 = TreeNode(1,firstTreeNode2, None)
secondTreeNode1 = TreeNode(1,None, secondTreeNode2)

treeRoot = TreeNode(1, firstTreeNode1, secondTreeNode1)

obj = Solution()
print(obj.isSymmetric(treeRoot))