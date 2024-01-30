def solve(numbers):
    pairs = 0
    hashmap = dict()
    for i in range(0, len(numbers)):
        difference = numbers[i] - i
        if difference not in hashmap:
            hashmap[difference] = 1
        else:
            hashmap[difference] += 1
    
    for i in range(0,len(numbers)):
        difference = numbers[i] - i
        if difference in hashmap and hashmap[difference]  > 1:
            pairs += (hashmap[difference] - 1)
    
    return pairs//2

cases = int(input())
while cases > 0:
    n = int(input())
    nums = list(map(int,input().split(' ')))
    print(solve(nums))
    cases -= 1    
            