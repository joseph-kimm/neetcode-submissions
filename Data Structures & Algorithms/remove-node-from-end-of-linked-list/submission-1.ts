/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head: ListNode | null, n: number): ListNode {

        // becuase going n steps leads us to the exact one to remove,
        // we do n+1 steps to ensure we stop at the previous one

        let first = head
        let second = head

        if (!head.next) {
            return null
        }

        for (let i = 0; i < n; i++) {
            first = first.next
        }

        if (!first) {
            return head.next
        }
        
        while (first && first.next) {
            first = first.next
            second = second.next
        }

        second.next = second.next.next

        return head



        
        
    }
}
