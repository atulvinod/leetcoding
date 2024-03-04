def factorial(n):
    if n <= 0:
        return 1
    return n*factorial(n-1)

def  binomialCoeff(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def pascalsTriangle(startIndex):
    spacing = 0
    for n in range(startIndex-1, -1, -1):
        pascalRow= []
        for r in range(n, -1, -1):
            coeffValue = binomialCoeff(n, r)
            pascalRow.append(str(round(coeffValue)))
        print((" "*spacing)+" ".join(pascalRow))
        spacing += 1

pascalsTriangle(7)