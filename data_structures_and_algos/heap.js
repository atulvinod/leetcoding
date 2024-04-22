class Heap {
    constructor(array) {
        this.heap = this.#heapify(array)
    }


    #processHeap(array, index) {
        if (index == 0) {
            return;
        }
        let parent = Math.floor((index - 1) / 2)
        if (array[index] > array[parent]) {
            [array[index], array[parent]] = [array[parent], array[index]]
            return this.#processHeap(array, parent)
        }
    }

    pop() {
        if (this.heap.length == 0) {
            return null
        }
        let heap = [...this.heap]
        let end = heap.length - 1;
        [heap[0], heap[end]] = [heap[end], heap[0]]
        let value = heap.pop()
        let index = 0
        while (true) {
            let left = 2 * index + 1
            let right = 2 * index + 2
            let largest = index;
            if (left < heap.length && heap[left] > heap[largest]) {
                largest = left
            }
            if (right < heap.length && heap[right] > heap[largest]) {
                largest = right
            }

            if (largest != index) {
                [heap[index], heap[largest]] = [heap[largest], heap[index]]
                index = largest
            } else {
                break;
            }
        }
        this.heap = [...heap]
        return value
    }

    /**
     * 
     * @param {Array<Number>} array 
     */
    #heapify(array) {
        let arr = [...array]
        for (let i = arr.length - 1; i > 0; i--) {
            this.#processHeap(arr, i)
        }
        return arr
    }
}

const heap = new Heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
console.log(heap.pop())
console.log(heap.pop())
console.log(heap.pop())
console.log(heap.pop())
console.log(heap.pop())