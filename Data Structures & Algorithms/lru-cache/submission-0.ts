class LinkNode {
    key: number
    val: number
    next: LinkNode
    prev: LinkNode

    constructor(key: number, val:number) {
        this.key = key
        this.val = val
    }
}

class LRUCache {

    map = new Map<number,LinkNode>();
    least_rec = new LinkNode(0,0);
    most_rec = new LinkNode(0,0);
    capacity

    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.least_rec.next = this.most_rec
        this.most_rec.prev = this.least_rec
        this.capacity = capacity
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {

        if (!this.map.has(key)) {
            return -1
        }

        // finding the value
        const node = this.map.get(key)

        // take node out
        node.prev.next = node.next
        node.next.prev = node.prev

        // insert node 
        node.prev = this.most_rec.prev
        node.prev.next = node
        node.next = this.most_rec
        this.most_rec.prev = node

        return node.val;
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {

        let node: LinkNode;
        if (this.map.has(key)) {
            node = this.map.get(key)
            node.val = value

            // take node out
            node.prev.next = node.next
            node.next.prev = node.prev

        }

        else {
            node = new LinkNode(key, value);
            this.map.set(key, node);
        }

        // insert node
        node.prev = this.most_rec.prev
        node.prev.next = node
        node.next = this.most_rec
        this.most_rec.prev = node

        // take least recently used node out
        if (this.map.size > this.capacity) {
            const least_node = this.least_rec.next
            this.least_rec.next = least_node.next
            least_node.next.prev = this.least_rec

            this.map.delete(least_node.key)
        }

        return

    }
}
