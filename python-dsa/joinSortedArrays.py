a = [1, 1, 2, 5, 6, 8, 9]
b = [1, 2, 6, 9, 10, 12]
result = []
aIndex, bIndex = 0, 0

while aIndex < len(a) and bIndex < len(b):
    currentA = a[aIndex]
    currentB = b[bIndex]
    if a[aIndex] == b[bIndex]:
        result.append(a[aIndex])
        aIndex = aIndex + 1
        bIndex = bIndex + 1
    elif a[aIndex] < b[bIndex]:
        result.append(a[aIndex])
        aIndex = aIndex + 1
    else:
        result.append(b[bIndex])
        bIndex = bIndex + 1
        
    while aIndex < len(a) and a[aIndex] == currentA:
        aIndex = aIndex + 1
    while bIndex < len(b) and a[bIndex] == currentB:
        bIndex = bIndex + 1


while aIndex < len(a):
    result.append(a[aIndex])
    aIndex = aIndex + 1

while bIndex < len(b):
    result.append(b[bIndex])
    bIndex = bIndex + 1

print(result)
