# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    written by amitjha@umich.edu
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        temp_lst = head
        out = head
        dummyNode = ListNode(0)
        tail = dummyNode
        while temp_lst:
            temp.append(temp_lst.val)
            temp_lst = temp_lst.next
        
        for val in temp[::-1]:
            tail.next = ListNode(val)
            tail = tail.next
        return(dummyNode.next)