# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return(0)
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)        
        
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right) 
        # print(height, ldiameter, rdiameter)
        return(max(lheight + rheight, max(ldiameter, rdiameter)) )
            
    def height(self, root):
        if not root:
            return(0)
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        return(max(lheight, rheight) + 1)