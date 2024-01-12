
//   Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var swap = function (nodeList, start, end) {
    let temp = nodeList[start]
    nodeList[start] = nodeList[end]
    nodeList[end] = temp;
}

var reverse = function (nodeList, start, end) {
    if (start >= end) {
        return;
    }
    let preStart = nodeList[start - 1] == undefined ? null : nodeList[start-1]
    let preEnd = nodeList[end - 1] == undefined ? null :nodeList[end-1]
    let nextStart = nodeList[start + 1] == undefined ? null : nodeList[start+1]
    let nextEnd = nodeList[end + 1] == undefined ? null : nodeList[end+1]

    if (nodeList[start] == preEnd && nodeList[end] == nextStart) {
        if (preStart)
            preStart.next = nodeList[end];
        if (nodeList[start])
            nodeList[start].next = nextEnd;
        if (nodeList[end])
            nodeList[end].next = nodeList[start]
    } else {
        if (preStart)
            preStart.next = nodeList[end]
        if (nodeList[end])
            nodeList[end].next = nextStart;
        if (preEnd)
            preEnd.next = nodeList[start]
        if (nodeList[start])
            nodeList[start].next = nextEnd
    }


    swap(nodeList, start, end)
    return reverse(nodeList, start + 1, end - 1)
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function (head, k) {
    let root = new ListNode(-1)
    root.next = head;
    let ptr = root;
    let nodeList = []
    while (ptr != null) {
        nodeList.push(ptr)
        ptr = ptr.next;
    }
    let start = 1;
    while (true) {
        let end = start + k - 1;
        if (end >= nodeList.length) {
            break;
        } else {
            reverse(nodeList, start, end)
        }
        start = end + 1;
    }
    return nodeList[1]
};

var listBuilder = (list) => {
    let head = null, tail = null;
    for (let l of list) {
        let node = new ListNode(l)
        if (!head) {
            head = node;
            tail = node
        } else {
            tail.next = node;
            tail = node;
        }
    }

    return head;
}

reverseKGroup(listBuilder([1, 2]), 2)