# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good=0
        
        max=root.val

        def dfs(root,max):
            nonlocal good
            if not root:
                return
            if root.val>=max:
                max=root.val
                good+=1
            dfs(root.left,max)
            dfs(root.right,max)
        dfs(root,max)
        return good
        