
class Node{
    index;
    value;
    lowest_pop;

    constructor(index, value, lowest_pop){
        this.lowest_pop = lowest_pop ?? index;
        this.index = index;
        this.value = value;
    }
}

var StockSpanner = function() {
    this.stack = []
    this.current_index = 1;
};

/** 
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
    /**
     * We pop all the elements which are lesser than price until we reach a greater element,
     * while popping all the elements, we keep track of 'lowest_pop' ie, the lowest index which 
     * was lesser than the current element;
     * 
     * if there is now lowest pop possible, we keep the index itself as the lowest_pop
     * 
     * eg
     *      31  41  48  59  79
     * i     0   1   2   3   4
     * lp    0   0   0   0   0
     * 
     * 
     *      100  80  60  70  60  75
     * i      0   1   2   3   4   5
     * lp     0   1   2   2   4   2
     */
   if(!this.stack.length){
        this.stack.push(new Node(0, price));
        this.current_index = 1;
        return 1;
   }

   let lowest_pop = this.current_index;

   while(this.stack.length && this.stack[this.stack.length-1].value <= price){
     lowest_pop = (this.stack.pop()).lowest_pop;
   }

   let result = this.current_index - lowest_pop + 1;
   this.stack.push(new Node(this.current_index, price, lowest_pop));
   this.current_index++;
   return result;
};

/** 
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */

let obj = null
let ops = ["StockSpanner","next","next","next","next","next"]
let args = [[],[31],[41],[48],[59],[79]]
for(let i = 0 ; i  < ops.length ; i++){
    if(ops[i] == 'StockSpanner'){
        obj = new StockSpanner()
    }else {
        console.log(obj.next(args[i][0]))
    }
}