# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next
        

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        temp = slow.next
        slow.next = None
        slow = temp

        if not slow:
            return



        # cut the end
        

        # flip the 2nd half
        prev = slow
        curr = prev.next
        prev.next = None

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        right = prev
        left = head

        i = 0
        while left and right:

            if i % 2 == 0:
                temp = left.next
                left.next = right
                left = temp
            
            else:
                temp = right.next
                right.next = left
                right = temp

            i += 1

        return

        




            
        