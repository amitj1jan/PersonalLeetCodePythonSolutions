# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0      
        mid = head
        temp = head
        while temp != None:
            if cnt &1:
                mid = mid.next
            cnt += 1
            temp = temp.next
        return(mid)
        
        
        