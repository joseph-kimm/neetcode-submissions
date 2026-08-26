// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head: Node | null): Node {

        if (!head) {
            return null
        }

        const mapping = new Map<Node,Node>();

        const new_head = new Node(head["val"])
        mapping.set(head, new_head)
        mapping.set(null, null)

        let curr = head["next"];
        let new_curr

        while (curr) {
            new_curr = new Node(curr["val"])
            mapping.set(curr, new_curr)
            curr = curr.next
        }

        curr = head
        while (curr) {
            new_curr = mapping.get(curr)
            new_curr.next = mapping.get(curr["next"])
            new_curr.random = mapping.get(curr["random"])
            curr = curr.next
        }

        return new_head
    }
}
