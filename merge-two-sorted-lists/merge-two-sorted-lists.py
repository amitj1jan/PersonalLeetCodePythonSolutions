# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    written by amitjha@umich.edu
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyNode = ListNode(0)
        tail = dummyNode
        while True:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break            
            if l1.val <= l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next
        return(dummyNode.next)
        