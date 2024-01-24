def solve(strings):
    result = ["0"]*len(strings)
    string_tuples = set(strings)
    strings = sorted([(value, index) for index, value in enumerate(strings)]
, key= lambda x : len(x[0]))
    
    for i in range(len(strings)-1, -1, -1):
        for k in range(len(strings[i][0])):
            x = strings[i]
            a = x[0][0:k+1]
            b = x[0][k+1:]
            if a in string_tuples and b in string_tuples:
                result[strings[i][1]] = "1"
                break
                
    final_result =  ''.join(result)
    return final_result

cases = int(input())
while cases > 0:
    strings = []
    string_count = int(input())
    while string_count > 0:
        s = input()
        strings.append(s)
        string_count -= 1
    print(solve(strings))
    cases -= 1
    
    
strings =  [

"codeforc",
"es",
"codes",
"cod",
"forc",
"forces",
"e",
"code"
]

solve(strings)