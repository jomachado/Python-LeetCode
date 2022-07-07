from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root == None):
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        backup = root.left
        root.left = root.right
        root.right = backup

        return root

    def printTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            levelStr = dict()
            printString = ""
            def printTreeSub(root, level):            
                if(root == None):
                    return
                if(level not in levelStr):
                    levelStr[level] = str(root.val)+","
                else:    
                    levelStr[level] += str(root.val)+","
                printTreeSub(root.left, level+1)        
                printTreeSub(root.right, level+1)
            printTreeSub(root,0)
      
            for item in levelStr:
                printString += levelStr[item]
            print(printString[0:-1], end="\n")           



Node1 = TreeNode(1, None, None)
Node3 = TreeNode(3, None, None)

Node2 = TreeNode(2, Node1, Node3)

Node6 = TreeNode(6, None, None)
Node9 = TreeNode(9, None, None)

Node7 = TreeNode(7, Node6, Node9)
Node4 = TreeNode(4, Node2, Node7)

obj = Solution()
obj.printTree(Node4)
obj.invertTree(Node4)
print("ínvertida,")
obj.printTree(Node4)