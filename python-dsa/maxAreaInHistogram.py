def histogramArea(numbers):
    stack = []
    previousLower = [-1 for _ in range(0, len(numbers))]
    nextLower = [len(numbers) for _ in range(0, len(numbers))]
    
    for i in range(0, len(numbers)):
        while len(stack) != 0  and numbers[stack[-1]] > numbers[i]:
            stack.pop()
        if len(stack) != 0:
            previousLower[i] = stack[-1]
        stack.append(i)
            
    stack.clear()
    for i in range(0, len(numbers)):
        while len(stack) != 0 and numbers[stack[-1]] > numbers[i]:
            greaterIndex = stack.pop()
            nextLower[greaterIndex] = i
        stack.append(i)
        
    area = 0
    for i in range(len(numbers)):
        cur = (nextLower[i] - previousLower[i] - 1)*numbers[i]
        area = max(area,cur)
    return area
        
    
histogramArea([1,2,1,0,1,1,0,0,2,2,])
    
    
    