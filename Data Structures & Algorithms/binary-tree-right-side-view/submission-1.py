# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right=[]
        heap=deque([root])

        while heap:
            right.append(heap[len(heap)-1].val)

            for i in range(len(heap)):
                node=heap.popleft()

                if node.left:
                    heap.append(node.left)
                if node.right:
                    heap.append(node.right)
            

        return right
        