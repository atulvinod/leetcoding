def solve(arr):
    previous_smaller_element = [-1]*len(arr)
    next_smaller_element = [len(arr)]*len(arr)
    stack = []
    
    # to calculate the previous smaller element 
    for i in range(len(arr)):
        while len(stack) != 0 and  arr[i] < arr[stack[-1]]:
            stack.pop()
        if len(stack) != 0:
            previous_smaller_element[i] = stack[-1] 
        stack.append(i)
    
    stack.clear()
    # to calculate the next smaller element
    for i in range(len(arr)):
        while len(stack) != 0 and arr[i] < arr[stack[-1]]:
            top_element_index = stack[-1]
            next_smaller_element[top_element_index] = i
            stack.pop()
        stack.append(i)
        
    area = 0
    for i in range(len(arr)):
        cur = (next_smaller_element[i] - previous_smaller_element[i] - 1)*arr[i]

        area = max(area,cur)
    
    return area
        
    
solve([1,2,1,0,1,1,0,0,2,2,])
    
    
    