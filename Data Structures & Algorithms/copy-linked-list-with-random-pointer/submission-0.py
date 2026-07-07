"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        mp={}
        curr=head
        while curr:
            mp[curr]=Node(curr.val)
            curr=curr.next
        
        for node in mp:
            mp[node].next=mp.get(node.next)
            mp[node].random=mp.get(node.random)
        
        return mp[head]



        