def solve(numbers):
    countOfNegativeNumbers = 0
    absoluteSum = 0
    smallestNumber = float('inf')
    for i in numbers:
        if i < 0:
            countOfNegativeNumbers += 1
        absoluteSum += abs(i)
        smallestNumber = min(smallestNumber, abs(i))
        
    if countOfNegativeNumbers % 2 == 0:
        return absoluteSum
    
    absoluteSum = absoluteSum - 2*smallestNumber
    return absoluteSum

testcases = int(input())

while testcases > 0:
    n = int(input())
    arr = input().split(' ')
    num_arr = [int(n) for n in arr]
    print(solve(num_arr))
    testcases -= 1
         
            
# remains same
        
        