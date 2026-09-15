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
     * @return {boolean}
     */
    isValidBST(root: TreeNode | null): boolean {

        function dfs(node: TreeNode, left:number, right:number): boolean {
            if (!node) {
                return true
            }

            if (node.val >= right || node.val <= left) {
                return false
            }

            return dfs(node.left, left, node.val) && dfs(node.right, node.val, right)
        }

        return dfs(root, -Infinity, +Infinity)
    }
}
