'''
Fenwick trees allow us to efficiently compute the sum for a range (l,r)
Fenwick tree uses bit array to store this range data

> to get the number after removing last bit of a number i
n = i - (i & -i)
-i is the 2s complement of i (aka negative number, 2s complement is calculated by taking complement of a number + 1)
when we do (i & -i)  we get the mask where only the last bit of the number is set, hence when we subtract this
number from the original number to get the number 'n' which represents the value we get by removing the last 
bit of number 'i'. Similarly if we add this number, we get a number 'n' whose value represents the value 
if we set the last bit of number 'i'

> bit[i] stores data from j + 1 -> 1, where j is the number we get after removing last bit of i

> to update a value in a fenwick tree, we use the delta to update the index (original value at ith index at main array - updated value) to propagate the change, as it will modify the subsequent dependent ranges

'''


class FenwickTree:
    
    def __init__(self, array) -> None:
        self.array = array
        self.bitTree = self.createFenwickTree(array)
        
        
    def createFenwickTree(self, array):
        bitTree = [0]*(len(array) + 1)
        
        def update(index, delta):
            while index < len(bitTree):
                bitTree[index] += delta
                
                # by using this operation, we also update the indexes which 
                # store the computed value where our current index also contributes to
                # eg, if we update the index 13, we also need to update the 14th index because
                # 14th index uses the 13th index to compute the sum value
                index += (index & -index)
                
        for n in range(1, len(array)+1):
            update(n, array[n - 1])
        
        return bitTree

    def query(self, l, r):
        
        def sum(index):
            ans = 0
            while index > 0:
                ans += self.bitTree[index]
                # we accumulate the values of the parent indexes as well
                index -= (index & -index)
            return ans
        
        return sum(r) - sum(l-1) 
    
array = [1,2,3,4,5,6,7,8,9,10]
fwt = FenwickTree(array)
# based on 1 index
print(fwt.query(1,2))