
const {TreeNode, treeFromArray} = require('./treebuilder');

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function (root) {
    const result = []
    if (!root) {
        return result;
    }
    const stack = []
    let ptr = root;
    while (ptr != null || stack.length ) {
        while (ptr != null) {
            stack.push(ptr);
            ptr = ptr.left;
        }
        ptr = stack.pop()
        result.push(ptr.val);
        ptr = ptr.right;
    }
    return result;
};


inorderTraversal(treeFromArray([1, null, 2, 3]))