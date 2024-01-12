
//   Definition for a binary tree node.
function Node(data) {
    this.data = data;
    this.left = null;
    this.right = null;
}

/**
 * 
 * @param {Node} node 
 * @param {Number} row 
 * @param {Number} col 
 */
function GridNode(node, row, col) {
    this.node = node;
    this.row = row;
    this.col = col
}

/**
 * @param {Node} root
 * @return {number[][]}
 */
var verticalTraversal = function (root) {
    let queue = []
    let map = {}
    queue.push(new GridNode(root, 0, 0));
    map[0] = [root.data]
    let minCol = 0
    let maxCol = 0;
    while (queue.length) {
        let length = queue.length;
        while (length--) {
            let { node, row, col } = queue.shift();
            if (node.left) {
                queue.push(new GridNode(node.left, row + 1, col - 1))
                if (!map[col - 1]) {
                    map[col - 1] = []
                }
                map[col - 1].push(node.left.data);

                minCol = Math.min(minCol, col - 1)
            }
            if (node.right) {
                queue.push(new GridNode(node.right, row + 1, col + 1))
                if (!map[col + 1]) {
                    map[col + 1] = []
                }
                map[col + 1].push(node.right.data);
                maxCol = Math.max(maxCol, col + 1)
            }
        }
    }

    let result = []
    for (let i = minCol; i <= maxCol; i++) {
        let rows = map[i];
        result.push(rows[0]);
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
            map[i] = new Node(array[i]);
        }
        root = map[i];
        if (left <= array.length - 1 && array[left] != null) {

            let left_node = null;
            if (!map[left]) {
                map[left] = new Node(array[left]);
            }
            left_node = map[left];
            root.left = left_node;
        }
        if (right <= array.length - 1 && array[right] != null) {
            let right_node = null;
            if (!map[right]) {
                map[right] = new Node(array[right]);
            }
            right_node = map[right];
            root.right = right_node;
        }
    }

    return map[0];
}

verticalTraversal(treebuilder([1, 2, 3, 4, 5, 6, 7]))