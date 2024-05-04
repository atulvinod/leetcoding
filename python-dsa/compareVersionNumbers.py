from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        version1str: List[int] = list(map(int, list(version1.split("."))))
        version2str: List[int] = list(map(int, list(version2.split("."))))

        maxLength = max(len(version1str), len(version2str))
        version1str.extend([0] * (maxLength - len(version1str)))
        version2str.extend([0] * (maxLength - len(version2str)))

        for v in range(len(version1str)):
            if version1str[v] > version2str[v]:
                return 1
            elif version2str[v] > version1str[v]:
                return -1
        return 0


s = Solution()
print(s.compareVersion(version1="0.1", version2="1.1"))
