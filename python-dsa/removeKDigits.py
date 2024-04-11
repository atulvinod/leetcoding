class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        for i in range(len(num)):
            while len(stack) != 0 and k != 0 and num[i] < stack[-1]:
                stack.pop()
                k = k - 1
            stack.append(num[i])
        stack = stack[:-k] if k > 0 else stack
        result = "".join(stack).lstrip("0")
        return result if result else "0"
