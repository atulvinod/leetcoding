function prevSmaller(nums) {
    const stack = [];
    let result = []
    for (let i = 0; i < nums.length; i++) {
        while (stack.length && stack[stack.length - 1] >= nums[i]) {
            stack.pop()
        }
        if (!stack.length) {
            result.push(-1)
            stack.push(nums[i])
        } else {
            result.push(stack[stack.length - 1])
            stack.push(nums[i])
        }
    }

    return result;
}


prevSmaller([4,5,2,10,8])