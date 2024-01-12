class Solution 
{
    
  
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    maxMeetings(start, end, n)
    {

        function solve(startIndex, start, end){
            let count = 1
            // code here
            let current = []
            for(let i  = startIndex ; i < n ; i++){
                if(!current.length){
                    current = [start[i],end[i]]
                }else{
                    if(start[i]>current[1]){
                        count++;
                        current = [start[i],[end[i]]]
                    }
                }
            }
            
            return count;
        }


        let max = 1;
        for(let i = 0 ; i < n ;i++){
            max = Math.max(solve(i,start,end),max)
        }
        return max;
    }
}
maxMeetings([1,3,0,5,8,5],[2,4,6,7,9,9],6)