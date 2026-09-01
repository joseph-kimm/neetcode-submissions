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
     * @param {number} k
     * @return {ListNode}
     */
    reverseKGroup(head: ListNode | null, k: number): ListNode {

        const dummy = new ListNode();
        
        let connect = dummy; // end of all reversed so far

        let start = head; // start of a new reverse 

        let curr = head; // current node to switch 
        let prev; // prev node to connect next to

        let present = true;
        
        while (true) {

            let check = curr

            // checking if there are k nodes
            for (let i = 0;i < k; i++) {
                if (check) {
                    check = check.next
                }

                else {
                    present = false
                    break
                }
            }

            if (!present) {
                break
            }

            prev = curr
            curr = curr.next
            prev.next = null

            for (let i = 1;i < k; i++) {

                // reverse node
                let temp = curr.next

                curr.next = prev
                prev = curr
                curr = temp
            }

            connect.next = prev
            connect = start

            start = curr  
        }

        connect.next = curr
        return dummy.next
    }
}
