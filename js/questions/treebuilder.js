function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

function treeFromArray(array) {
    if (array.length === 0)
      return null;
  
    let nextItem = 0;
    const root = new TreeNode(array[nextItem++]);
    const queue = [root];
  
    while (queue.length > 0 && nextItem < array.length) {
      const current = queue.shift();
  
      if (nextItem < array.length) {
        const item = array[nextItem++];
  
        if (item !== null) {
          const node = new TreeNode(item);
          current.left = node;
          queue.push(node);
        }
      }
  
      if (nextItem < array.length) {
        const item = array[nextItem++];
  
        if (item !== null) {
          const node = new TreeNode(item);
          current.right = node;
          queue.push(node);
        }
      }
    }
  
    return root;
  }

module.exports = {TreeNode, treeFromArray}