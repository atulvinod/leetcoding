
class Node {
    key;
    value;
    next;
    prev;
    freq = 1;
    constructor(key,value){
        this.key = key;
        this.value = value;
    }
}

class lfuQueue{
    head = new Node('head')
    tail = new Node('tail')
    capacity = 0;

    /**
     * 
     * @param {Node} node 
     */
    insertBack(node){
        if(!this.capacity){
            this.head.next = node
            this.tail.prev = node;
            node.next = this.tail;
            node.prev = this.head;
            this.capacity = 1;
        }else{
            this.tail.prev.next = node;
            node.prev = this.tail.prev;
            node.next = this.tail
            this.tail.prev = node;
            this.capacity++;
        }
    }

    delete(node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
        this.capacity--;
    }

    pop(){
        if(!this.capacity){
            return null;
        }
        let node = this.head.next;
        this.head.next = node.next;
        node.next.prev = this.head;
        this.capacity--;
        return node;
    }

    peekFront(){
        if(!this.capacity){
            return null;
        }

        return this.head.next;
    }

    peekBack(){
        if(!this.capacity){
            return null
        }

        return this.tail.prev;
    }

    getCapacity(){
        return this.capacity;
    }

    insertFront(node){
        node.next = this.head.next;
        node.prev = this.head;
        this.head.next = node;
        this.capacity++;
    }
}

/**
 * @param {number} capacity
 */
var LFUCache = function(capacity) {
    this.max_capacity = capacity;
    this.current_capacity = 0;
     /**
     * @type {{[key:Number]:lfuQueue}}
     */
    this.freq_cache_map = {1:new lfuQueue()}

    /**
     * @type {{[key:String]:Node}}
     */
    this.node_map = {}
    this.current_lowest_freq = 1;
    this.freq_array = [1]
};

/** 
 * @param {number} key
 * @return {number}
 */
LFUCache.prototype.get = function(key) {
    console.log(`get k:${key}`)

    if(!this.node_map[key]){
        return -1;
    }
    let node = this.node_map[key];
    this.updateNodeFreq(node);
    return node.value
};

LFUCache.prototype.updateNodeFreq = function(node){
    let queue = this.freq_cache_map[node.freq];
    node.freq++;
    queue.delete(node);
    if(!this.freq_cache_map[node.freq]){
        this.freq_cache_map[node.freq] = new lfuQueue();
    }
    let next_queue = this.freq_cache_map[node.freq]
    next_queue.insertBack(node)
    if(this.freq_array[this.freq_array.length-1] < node.freq){
        this.freq_array.push(node.freq);
    }
}

LFUCache.prototype.handleLowestFreqPop = function(){
    let queue = this.freq_cache_map[this.current_lowest_freq];
    let delete_node = null;
    if(!queue || !queue.capacity){
        for(let  i = this.current_lowest_freq -1 ; i < this.freq_array.length; i++){
            queue = this.freq_cache_map[this.freq_array[i]];
            if(queue && queue.capacity){
                this.current_lowest_freq = i;
                delete_node = queue.pop()
                break;
            }
        }
    }
    if(!delete_node && queue && queue.capacity){
        delete_node = queue.pop();
    }
    if(delete_node){
        delete this.node_map[delete_node.key];
    }
}

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LFUCache.prototype.put = function(key, value) {
    console.log(`put k:${key} v:${value}`)
    let new_node = new Node(key, value)
    if(this.node_map[key]){
        let node = this.node_map[key];
        node.value = value;
        this.updateNodeFreq(node);
        return;
    }

    this.node_map[key] = new_node;
    // to check if new element can be inserted
    if(this.current_capacity < this.max_capacity){
        this.current_capacity++;
    }else{
        // pop from the lowest freq;
        this.handleLowestFreqPop()
    };

    let queue = this.freq_cache_map[1];
    queue.insertBack(new_node);
};

/** 
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */


var obj = null;

let ops = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]


let args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

for(let i = 0 ; i < ops.length ; i++){
    if(ops[i]=='put'){
        obj.put(args[i][0], args[i][1])
    }else if(ops[i] == 'get'){
        console.log('result: ',obj.get(args[i][0]))
    }else{
        obj = new LFUCache(args[i][0])
    }
}   