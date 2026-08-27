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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode {

        let place = l1
        let sum = 0;
        let over = 0
        let prev;

        while (l1 && l2) {
            sum = l1.val + l2.val + over

            over = Math.trunc(sum / 10)
            sum = sum % 10

            l1.val = sum

            if (!l1.next) {
                prev = l1
            }

            l1 = l1.next
            l2 = l2.next
        }
        
        if (l2) {
            prev.next = l2
            l1 = l2
        }

        while (l1) {
            sum = l1.val + over
            over = Math.trunc(sum / 10)
            sum = sum % 10

            l1.val = sum

            if (!l1.next) {
                prev = l1
            }

            l1 = l1.next
        }

        if (over != 0) {
            const overNode = new ListNode(over)
            prev.next = overNode
        }

        return place;
    }
}
