# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #split
        second = slow.next
        slow.next = None

        #reverse
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge
        second = prev
        while head and second:
            a = head.next 
            b = second.next
            head.next = second
            second.next = a
            head = a 
            second = b