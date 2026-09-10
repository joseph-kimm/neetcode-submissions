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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {

        function sameTree (a:TreeNode, b:TreeNode): boolean {

            if (!a && !b) {
                return true
            }

            else if (!a || !b) {
                return false
            }

            else if (a.val != b.val) {
                return false
            }

            const left = sameTree(a.left, b.left)
            const right = sameTree(a.right, b.right)

            return left && right
        }

        function dfs(root: TreeNode, subRoot: TreeNode): boolean {
            if (!root && !subRoot) {
                return true
            }

            else if (!root || !subRoot) {
                return false
            }

            const curr = sameTree(root, subRoot)
            const left = dfs(root.left, subRoot)
            const right = dfs(root.right, subRoot)

            return curr || left || right
        }

        return dfs(root, subRoot)
    }
}
