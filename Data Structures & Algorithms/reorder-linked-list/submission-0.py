# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head1=head
        slow,fast=head1,head1
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        partition2=slow.next
        slow.next=None
        partition1=head1

        prev=None
        curr=partition2
        
        while curr:
            nxt=curr.next
            curr.next=prev
            
            prev=curr
            curr=nxt
        partition1=head   
        partition2=prev
        
        while partition1 and partition2:
            nxt1=partition1.next
            nxt2=partition2.next

            partition1.next=partition2
            partition2.next=nxt1
            partition1=nxt1
            partition2=nxt2
       
        return 

            
        


        