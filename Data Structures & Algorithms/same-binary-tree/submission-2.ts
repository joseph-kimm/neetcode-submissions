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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {

        // depth first search

        function dfs(p:TreeNode,q:TreeNode): boolean{
            if (!p && !q) {
                return true
            }

            else if (!p || !q) {
                return false
            }

            else if (p.val != q.val) {
                return false
            }

            const left = dfs(p.left, q.left)
            const right = dfs(p.right, q.right)

            return left && right

        }

        return dfs(p,q)
        
    }
}
