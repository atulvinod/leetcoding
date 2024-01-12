
/* Declare and implement your function here 
eg: function example(parameter_name1,parameter_name2....){}
Handle the input/output from main()
*/




process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}


function Node(value) {
    this.next = null;
    this.prev = null;
    this.value = value;
}

function Queue() {
    this.head = new Node('head');
    this.tail = new Node('tail')
    this.head.next = this.tail;
    this.tail.prev = this.head;
}

Queue.prototype.peekFront = function () {
    if (this.head.next == this.tail) {
        return null;
    }
    return this.head.next.value;
}

Queue.prototype.popFront = function () {
    if (this.head.next == this.tail) {
        return null;
    }

    let node = this.head.next;
    this.head.next = node.next;
    node.next.prev = this.head;
    return node.value;
}

Queue.prototype.popBack = function () {
    if (this.head.next == this.tail) {
        return null;
    }
    let node = this.tail.prev;
    this.tail.prev = node.prev;
    node.prev.next = this.tail;
    return node.value;
}

Queue.prototype.peekBack = function () {
    if (this.head.next == this.tail) {
        return null;
    }
    return this.tail.prev.value;
}

Queue.prototype.pushBack = function (node) {
    let last_node = this.tail.prev;
    last_node.next = node;
    node.prev = last_node;
    this.tail.prev = node;
}

Queue.prototype.isEmpty = function () {
    return this.head.next == this.tail;

}

function main() {

    /* Read your input here 
    eg: For string variables:   let str = String(readLine()); 
        For int variables: let var_name = parseInt(readLine());
        For arrays : const arr = readLine().replace(/\s+$/g, '').split(' ');
    */

    /*
    Call your function with the input/parameters read above
    eg: let x = example(var_name, arr);
    */

    /*
    Log your output here 
    eg: console.log(x);
    */


    /**
     * 
     * @param {Array} array 
     * @param {Number} k 
     */
    function getMaxOfMinimumsOfWindow(array, k) {
        if (k == 1) {
            let max = Number.MIN_SAFE_INTEGER;
            array.forEach(i => {
                max = Math.max(max, i)
            })
            return max;
        } else if (k == array.length) {
            let min = Number.MAX_SAFE_INTEGER;
            array.forEach(i => {
                min = Math.min(min, i)
            })
            return min;
        }

        const queue = new Queue();
        const minimums_of_window = []
        let maximum_of_minimums = Number.MIN_SAFE_INTEGER;
        for (let i = 0; i < array.length; i++) {
            while (!queue.isEmpty() && queue.peekFront() < (i - k + 1)) {
                queue.popFront();
            }
            while (!queue.isEmpty() && array[queue.peekBack()] > array[i]) {
                queue.popBack();
            }
            queue.pushBack(new Node(i));
            if (i >= k - 1) {
                let front_value = queue.peekFront();
                // minimums_of_window.push(array[front_value])
                maximum_of_minimums = Math.max(maximum_of_minimums, array[front_value]);
            }
        }
        //    console.log(minimums_of_window);
        return maximum_of_minimums;
    }

    /**
     * 
     * @param {Array} array 
     */
    function solve(array) {
        let result = []
        for (let i = 1; i <= array.length; i++) {
            const maximum = getMaxOfMinimumsOfWindow(array, i);
            result.push(maximum);
        }
        return result;
    }

    let test_case_count = parseInt(readLine());
    while (test_case_count--) {
        const n = parseInt(readLine());
        const arr = readLine().replace(/\s+$/g, '').split(' ')
        const result = solve(arr);
        console.log(result.join(' '))
    }
}
','.replace()

main()