const {TreeNode} = require('./treebuilder');

var bstFromPreorder = function (preorder) {
    // init the root using the first value in the preorder treee
    // as first element is the root of the tree in preorder traversal
    let root = new TreeNode(preorder[0]);
    if (preorder.length == 1) {
        return root;
    }
    for (let i = 1; i < preorder.length; i++) {
        let new_node = new TreeNode(preorder[i]);
        let ptr = root;
        while (true) {
            // if the value is less than the pointer value,
            // then check if the left node of the pointer is null,
            // if null then insert the node else shift the pointer 
            // to the left node to find the correct place to insert the value

            if (preorder[i] < ptr.val) {
                if (ptr.left == null) {
                    ptr.left = new_node;
                    break;

                } else {
                    ptr = ptr.left;
                }
            }
            if (preorder[i] > ptr.val) {
                if (ptr.right == null) {
                    ptr.right = new_node;
                    break;

                } else {
                    ptr = ptr.right;
                }
            }
        }
    }

    return root;
};