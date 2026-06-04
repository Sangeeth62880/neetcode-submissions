
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k = k - 1
        return curr
        
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # reverse k nodes
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # reconnect
            tmp = groupPrev.next  # old head = future new tail
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next