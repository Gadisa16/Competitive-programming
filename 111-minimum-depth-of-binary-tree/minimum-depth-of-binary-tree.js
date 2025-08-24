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

    let q = [[root, 1]];

    while (q.length) {
        let [node, dep] = q.shift(); //destructuring array

        if (!node.left && !node.right) return dep;
        
        if (node.left) q.push([node.left, dep+1]);

        if (node.right) q.push([node.right, dep+1]);
    }
};