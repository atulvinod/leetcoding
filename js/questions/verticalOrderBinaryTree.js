
//   Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * 
 * @param {TreeNode} node 
 * @param {Number} row 
 * @param {Number} col 
 */
function Node(node, row, col) {
    this.node = node;
    this.row = row;
    this.col = col
}

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var verticalTraversal = function (root) {
    let queue = []
    let map = {}
    queue.push(new Node(root, 0, 0));
    map[0] = { rows: { 0: [root.val] } }
    let minCol = 0
    let maxCol = 0;
    while (queue.length) {
        let length = queue.length;
        while (length--) {
            let { node, row, col } = queue.shift();
            if (node.left) {
                queue.push(new Node(node.left, row + 1, col - 1))
                if (!map[col - 1]) {
                    map[col - 1] = { rows: { [row + 1]: [node.left.val] } }
                } else {
                    if (!map[col - 1].rows[row + 1]) {
                        map[col - 1].rows[row + 1] = []
                    }
                    map[col - 1].rows[row + 1].push(node.left.val);
                }
                minCol = Math.min(minCol, col - 1)
            }
            if (node.right) {
                queue.push(new Node(node.right, row + 1, col + 1))
                if (!map[col + 1]) {
                    map[col + 1] = { rows: { [row + 1]: [node.right.val] } }
                } else {
                    if (!map[col + 1].rows[row + 1]) {
                        map[col + 1].rows[row + 1] = []
                    }
                    map[col + 1].rows[row + 1].push(node.right.val);
                }
                maxCol = Math.max(maxCol, col + 1)
            }
        }
    }

    let result = []
    for (let i = minCol; i <= maxCol; i++) {
        let {rows} = map[i];
        let temp = []
        let keys = Object.keys(rows);
        keys.forEach((key)=>{
            if(rows[key].length > 1){
                rows[key].sort((a,b)=>a-b)
            }
            temp.push(...rows[key]);
        })
        result.push(temp);
    }

    return result;
};


function treebuilder(array) {
    let map = {};
    for (let i = 0; i < array.length; i++) {
        if (array[i] == null) {
            continue;
        }

        let left = 2 * i + 1;
        let right = 2 * i + 2;
        let root = null
        if (!map[i]) {
            map[i] = new TreeNode(array[i]);
        }
        root = map[i];
        if (left <= array.length - 1 && array[left] != null) {

            let left_node = null;
            if (!map[left]) {
                map[left] = new TreeNode(array[left]);
            }
            left_node = map[left];
            root.left = left_node;
        }
        if (right <= array.length - 1 && array[right] != null) {
            let right_node = null;
            if (!map[right]) {
                map[right] = new TreeNode(array[right]);
            }
            right_node = map[right];
            root.right = right_node;
        }
    }

    return map[0];
}

treebuilder([28, null, 4, 42, 40, 39, 2, 24, 41, null, null, null, null, null, 17, 15, 37, 45, 18, null, 33, 43, 35, null, null, 23, null, null, null, null, null, null, 30, 12, null, null, null, null, 47, 7, null, null, 32, null, null ])
// verticalTraversal(treebuilder([1, 2, 3, 4, 5, 6, 7]))