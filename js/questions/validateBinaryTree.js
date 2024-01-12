const {TreeNode} = require('./treebuilder');

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
 * @return {boolean}
 */
var isValidBST = function (root) {
    const result = checkBst(root)
    return result.is_valid
};

var checkBst = function (root) {
    // to validate the whole binary tree, we also have to check if the sub
    // trees are also valid
    // maintain a absolute max value from left subtree and absolute min value
    // from right sub tree and check with the root value to find if the 
    // binary tree condition is valid
    
    let result = { is_valid: true, min: root.val, max: root.val };
    if (!root.left && !root.right) {
        return result;
    }
    let min_check = [root.val];
    let max_check = [root.val];

    if (root.left) {
        let left_tree = checkBst(root.left);
        if (!left_tree.is_valid || left_tree.max >= root.val) {
            result.is_valid = false;
            return result;
        }
        max_check.push(left_tree.max)
        min_check.push(left_tree.min);
    }

    if (root.right) {
        let right_tree = checkBst(root.right);
        if (!right_tree.is_valid || right_tree.min <= root.val) {
            result.is_valid = false;
            return result;
        }
        max_check.push(right_tree.max)
        min_check.push(right_tree.min);
    }
    result.max = Math.max(...max_check);
    result.min = Math.min(...min_check)
    return result;
}