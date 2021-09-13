# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        temp = head
        while temp:
            if temp.val in dic:
                prev.next = prev.next.next
                
            else:
                dic[temp.val] = 1
                prev = temp
            temp = temp.next
        return(head)