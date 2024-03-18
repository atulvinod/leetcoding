from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        stringMap = Counter(s)
        result = ""
        for index in range(len(order)):
            if order[index] in stringMap and stringMap[order[index]] > 0:
                result = result + (order[index] * stringMap[order[index]])
                stringMap[order[index]] = 0

        for key, count in stringMap.items():
            result = result + (key * count)
        return result


Solution().customSortString(order="kqep", s="pekeq")
