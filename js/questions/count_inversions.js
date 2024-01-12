function mergeSort(arr){
    if(arr.length==1){
        return {inv:0, arr}
    }

    let mid = parseInt(arr.length/2);
    let leftArr = arr.slice(0,mid);
    let rightArr = arr.slice(mid)
    let left = mergeSort(leftArr);
    let right = mergeSort(rightArr);

    let total = left.inv + right.inv;

    let finalArr = [];
    let leftPtr = 0
    let rightPtr = 0;

    // we use the merging function to count for the inversions
    // if the element at the right ptr is less than the element at the
    // left ptr, then all the elements at after the left ptr in the left array is also less
    // hence counted as inversion
    while(leftPtr<left.arr.length && rightPtr < right.arr.length){
        if(left.arr[leftPtr] < right.arr[rightPtr]){
            finalArr.push(left.arr[leftPtr++]);
        }else if(right.arr[rightPtr] < left.arr[leftPtr]){
            total += left.arr.length-leftPtr;
            finalArr.push(right.arr[rightPtr++])
        }else{
            finalArr.push(left.arr[leftPtr++])
            finalArr.push(right.arr[rightPtr++])
        }
    }

    while(leftPtr < left.arr.length){
        finalArr.push(left.arr[leftPtr++])
    }
    while(rightPtr < right.arr.length){
        finalArr.push(right.arr[rightPtr++])
    }
    return {inv:total, arr:finalArr};
}

mergeSort([2,5,1,3,4])