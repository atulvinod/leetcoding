
const {TreeNode, treeFromArray} = require('./treebuilder');

/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function (root) {
    const result = []
    if (!root) {
        return result;
    }
    const stack = []
    let ptr = root;
    while (ptr != null || stack.length ) {
        while (ptr != null) {
            result.push(ptr.val);
            stack.push(ptr);
            ptr = ptr.left;
        }
        ptr = stack.pop()
        ptr = ptr.right;
    }
    return result;
};


preorderTraversal(treeFromArray([1, null, 2, 3]))