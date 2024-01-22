def solve(number: int):
    result = ""
    while( number > 0 ):
        rem = number % 5
        result =  str(rem) + result
        number = number // 5
    return int("0" if result == "" else result)
        
    
inp = int(input())
print(solve(inp-1)*2)