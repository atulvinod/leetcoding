const {TreeNode} = require('./treebuilder');

/**
 * 
 * @param {TreeNode} root 
 */
const postOrderTraversal = (root)=>{
    let current = root;
    /**
     * @type {Array<TreeNode>}
     */
    let stack = []
    const result = []
    while(current != null || stack.length){
        // when current is not null, keep traversing the left
        // part of the tree
        if(current != null){
            stack.unshift(current);
            current = current.left;
        }else{
            // when current becomes null, check the stack to
            // see if there is a right subtree present, of the element which is at the top of the stack,
            // if there is, then we traverse that subtree
            let temp = stack[stack.length-1].right;
            
            if(temp == null){
                // if there is no right subtree
                // then we have reached either the leaf or root of the tree 
                temp = stack.pop();
                result.push(temp.val);

                // we check if the element that we popped just now is the right 
                // child of the element at the top of the stack.
                // if its the right of the element, then it implies we have traversed
                // the right tree as well, and the element at the top is the root element,
                // hence he have to pop the element and print it.
                // if its at the left of the element, then it implies that there might be a right subtree 
                // that we need to visit.

                // we keep it a loop to constantly pop all the nodes, if we are at the right side of the element 
                // at the top of the stack, because it implies we have traversed the right side of the tree
                while(stack.length && temp == stack[stack.length-1].right){
                    temp = stack.pop();
                    result.push(temp.val)
                }

            }else{
                current = temp;
            }
        }
    }
}