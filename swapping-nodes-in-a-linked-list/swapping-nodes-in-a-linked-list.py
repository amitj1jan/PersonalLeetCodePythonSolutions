# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow1,slow2, fast = head, head, head        
        for _ in range(k-1):
            slow1 = slow1.next
            fast = fast.next
            
        while fast.next:
            slow2 = slow2.next
            fast = fast.next
        
        slow1.val, slow2.val = slow2.val, slow1.val
        return(head)
            