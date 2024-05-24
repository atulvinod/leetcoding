from typing import List


def subsetsUsingBitmasking(array: List[int]):
    setSize = pow(2, len(array))
    subsets = []

    for bitMask in range(setSize):
        subset = []
        for bitPos in range(len(array)):
            if (bitMask & (1 << bitPos)) != 0:
                subset.append(array[bitPos])
        subsets.append(subset)

    print(subsets)


subsetsUsingBitmasking([1, 2, 3, 4])
