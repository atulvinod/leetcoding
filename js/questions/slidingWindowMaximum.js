class Node{
    index;
    value;
    next;
    prev;
    constructor(index, value){
        this.index = index;
        this.value = value;
    }
}

class sQueue{
    head = new Node(-1,'head')
    tail = new Node(-1, 'tail')
    constructor(){
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    /**
     * 
     * @param {Node} insert_point 
     * @param {Node} new_node 
     */
    insertBehindNode(insert_point, new_node){
        new_node.next = insert_point.next;
        new_node.prev = insert_point;
        insert_point.next.prev = new_node;
        insert_point.next = new_node;
    }

    validate(){
        let h_ptr = this.head;
        let t_ptr = this.tail;
        let h_path = []
        let t_path = []
        while(h_ptr){
            h_path.push(h_ptr.value)
            h_ptr = h_ptr.next;
        }
        while(t_ptr){
            t_path.unshift(t_ptr.value)
            t_ptr = t_ptr.prev;
        }
        console.log('h_path: ',h_path.join('->'))
        console.log('t_path: ',t_path.join('<-'))

    }

    /**
     * 
     * @param {Node} node 
     */
    insert(node){
        console.log('inserting ',node.value)
        if(this.head.next == this.tail){
            node.prev = this.head;
            node.next = this.tail;
            this.head.next = node;
            this.tail.prev = node;
            this.validate()
            return;
        }

        if(node.value > this.head.next.value){
            node.prev = this.head;
            node.next = this.head.next;
            this.head.next.prev = node;
            this.head.next = node;
            this.validate()
            return;
        }

        let ptr = this.tail.prev;
        while(ptr.value < node.value && ptr.next != this.head){
            ptr = ptr.prev;
        }
        this.insertBehindNode(ptr, node);
        this.validate()
    }

    getMax(start_index){
        let ptr = this.head.next;
        while(ptr.index < start_index && ptr.next != this.tail){
            ptr = ptr.next;
        }
        this.head.next = ptr;
        this.validate()
        console.log('get max ', ptr.value)
        return ptr.value;
    }
}



/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    let start = 0;
    let end = 0;
    let result = []
    let queue = new sQueue()
    while((end-start+1)<=k){
        let node = new Node(end, nums[end])
        queue.insert(node)
        end++;
    }

    while(end < nums.length){
        result.push(queue.getMax(start));
        let node = new Node(end, nums[end])
        queue.insert(node);
        end++;
        start++;
    }
    result.push(queue.getMax(start));
    return result;
};

// maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
maxSlidingWindow([1],1)