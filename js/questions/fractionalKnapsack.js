class Item{
    constructor(value, weight){
        this.value = value;
        this.weight = weight;
    }
}

class Solution 
{
    
    //Function to get the maximum total value in the knapsack.
    /**
 * @param {number} W
 * @param {Item[]} arr
 * @param {number} n
 * @returns {number}
*/
    fractionalKnapsack(W, arr, n)
    {
        arr.sort((a,b)=>{
            return parseInt(b.value/b.weight) - parseInt(a.value/a.weight)
        })

       

        let curWeight = 0;
        let finalValue = 0
        for(let i = 0 ; i < arr.length ; i++){
            if(curWeight + arr[i].weight <= W){
                curWeight += arr[i].weight;
                finalValue += arr[i].value
            }else{
                let remain = W - curWeight;
                finalValue += (arr[i].value * (remain / arr[i].weight))
            }
        }
        return finalValue;
    }
}

new Solution().fractionalKnapsack(50,[new Item(60,10), new Item(100,20), new Item(120,30)])