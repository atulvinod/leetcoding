
var search = function (nums, target) {
    let l = 0;
    let r = nums.length-1;
    
    while(l <= r){
        let mid =parseInt( (l+r)/2);
        if(target == nums[mid]){
            return mid;
        }
        // in an array A < B < C


        // for case where rotation C , B , A 
        if(nums[mid] > nums[r]){
              if (target < nums[mid] && target >= nums[l])
                r = mid - 1;
            else
                l = mid + 1;

        //for case where B, A, C
        }else if (nums[mid] < nums[l]){
              if (target > nums[mid] && target <= nums[r])
                l = mid + 1;
            else
                r = mid - 1;
        }else{
            // for the default general case where A, B, C
            if(target < nums[mid]){
                r = mid -1;
            }else{
                l = mid +1;
            }
        }
    }
    
    return -1;
}