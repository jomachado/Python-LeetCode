# Definition for a binary tree node.

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepthResult = 0  
        
        def maxDepthCustom(root: Optional[TreeNode], level):
            nonlocal maxDepthResult
            if(root == None):
                return None

            level +=1

            maxDepthResult = max(maxDepthResult, level)

            maxDepthCustom(root.left, level)
            maxDepthCustom(root.right, level)

        maxDepthCustom(root, 0)
        return maxDepthResult

firstTreeNode = TreeNode(3,None, None)
secondTreeNode = TreeNode(2,firstTreeNode, None)
treeRoot = TreeNode(1, None, secondTreeNode)

obj = Solution()
print(obj.maxDepth(treeRoot))