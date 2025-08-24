/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if (!root) return 0;

    function dfs(node, dep) {
        
        let rdepth = Infinity, ldepth = Infinity;

        if (!node.left && !node.right){
            return dep
        }

        if (node.left){
            ldepth = dfs(node.left, dep+1);
        }

        if (node.right) {
            rdepth = dfs(node.right, dep+1);
        }

        return Math.min(ldepth, rdepth);
    
    }

    return dfs(root, 1)
};