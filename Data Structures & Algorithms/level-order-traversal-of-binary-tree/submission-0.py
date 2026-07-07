# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result=[]
        heap=deque([root])

        while heap:
            lists=[]
            for i in range(len(heap)):
                node=heap.popleft()
                lists.append(node.val)

                if node.left:
                    heap.append(node.left)
                if node.right:
                    heap.append(node.right)

            result.append(lists)

        return result
        