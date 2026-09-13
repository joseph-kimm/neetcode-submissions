/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    goodNodes(root: TreeNode | null): number {

        function dfs(node: TreeNode | null, max: number): number {

            let res = 0

            if (!node) {
                return res
            }

            if (node.val >= max) {
                max = node.val
                res = 1
            } 

            return res + dfs(node.left, max) + dfs(node.right, max)
        }

        return dfs(root, root.val) 

    }
}
