# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return 

        heap = []
        dummy = ListNode()
        curr = dummy

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        counter = len(lists)

        while heap:
            val,i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next


        