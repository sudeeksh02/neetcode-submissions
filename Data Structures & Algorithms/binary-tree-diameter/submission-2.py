# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeheight(self,root):
        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1
        
        return 1+max(self.treeheight(root.left),self.treeheight(root.right))
    diameter=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left=self.diameterOfBinaryTree(root.left)
        right=self.diameterOfBinaryTree(root.right)

        curr=self.treeheight(root.left)+self.treeheight(root.right)

        return max(left,right,curr)
        