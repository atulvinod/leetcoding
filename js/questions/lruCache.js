/**
 * @class
 */
class Node{
    /**
     * @type {Number}
     */
    value = null;

    /**
     * @type {Node?}
     */
    next = null;

    /**
     * @type {Node?}
     */
    prev = null;

    key = null;
    constructor(key ,value, next, prev){
        this.value = value;
        this.key = key;
        this.next = next;
        this.prev = prev;
    }
}

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.head = new Node(null,'head');
    this.tail = new Node(null,'tail');
    this.head.next = this.tail;
    this.tail.prev = this.head;
    this.current_capacity = 0;
    /**
     * @type{ {[key:String]:Node]}}
     */
    this.map = {}
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    // console.log('get ',key)
    if(!this.map[key]){
        return -1;
    }

    let node = this.map[key];
    this.moveToEnd(node);
    // this.validate();
    return  node.value;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    // console.log('put ',key,' ',value);
    let new_node = new Node(key,value)
    let current_capacity = this.current_capacity;
    if(this.map[key]){
        this.map[key].value = value;
        this.moveToEnd(this.map[key]);
        return;
    }


    this.map[key] = new_node;
    if(current_capacity == this.capacity){
        //remove from head when capacity is reached
        let head_node = this.map[this.head.next.key];
        this.evictNode(head_node);
        this.current_capacity -= 1;
    }

    if( current_capacity == 0){
       this.handleEmptyCapacity(new_node);
       this.current_capacity = 1;
    }else{
       this.insertAtTail(new_node);
       this.current_capacity += 1;
    }
    this.validate();
};

LRUCache.prototype.insertAtTail = function(new_node){
    new_node.prev = this.tail.prev;
    new_node.next = this.tail;
    this.tail.prev.next = new_node;
    this.tail.prev = new_node;
}

LRUCache.prototype.evictNode = function(node){
    // console.log('evict k: ',node.key, ' v: ',node.value)
    delete this.map[node.key];
    this.head.next = node.next;
    node.next.prev = this.head;
}

LRUCache.prototype.moveToEnd = function(node){
    // merge adjacent nodes
    node.prev.next = node.next;
    node.next.prev = node.prev;

    //move to tail
    node.prev = this.tail.prev;
    node.next = this.tail;
    this.tail.prev.next = node;
    this.tail.prev = node;
}

LRUCache.prototype.handleEmptyCapacity = function(new_node){
    this.head.next = new_node;
    this.tail.prev = new_node;
    new_node.prev = this.head;
    new_node.next = this.tail;
}

LRUCache.prototype.validate = function(){
    let head_ptr = this.head;
    let tail_ptr = this.tail;
    let head_path = [];
    let tail_path = [];
    while(head_ptr){
        head_path.push( head_ptr.value);
        head_ptr  =head_ptr.next;
    }
    while(tail_ptr){
        tail_path.push( tail_ptr.value)
        tail_ptr  =tail_ptr.prev;
    }

    console.log('head_path: ',head_path.join('->'))
    console.log('tail_path :', tail_path.join('<-'))
}

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

var obj = new LRUCache(2);

let ops = ["LRUCache","put","put","put","put","get","get"]

let args = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

for(let i = 1 ; i < ops.length ; i++){
    if(ops[i]=='put'){
        obj.put(args[i][0], args[i][1])
    }else{
        console.log('result: ',obj.get(args[i][0]))
    }
}   