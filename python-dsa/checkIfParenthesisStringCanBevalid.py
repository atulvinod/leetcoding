class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        balance = 0

        # First check balance from left to right
        # For opening '(' brackets
        for i in range(n):
            # If either char is ( or it is unlocked,
            # We can increment balance
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            else:
                # otherwise decrement balance, since it is ) and also locked
                balance -= 1

            # Since balance is negative, we have more ')'.
            # And there is no unlocked char available
            # SO, it is an invalid string for sure
            if balance < 0:
                return False

        # reset balance
        balance = 0

        # Then also check balance from right to left
        # For closing ')' brackets
        for i in range(n - 1, -1, -1):
            # If either char is ) or it is unlocked,
            # We can increment balance
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            else:
                # otherwise decrement balance, since it is ( and also locked
                balance -= 1

            # Since balance is negative, we have more '('.
            # And there is no unlocked char available
            # SO, it is an invalid string for sure
            if balance < 0:
                return False

        return True

# Example Usage:
# solution = Solution()
# result = solution.canBeValid("((()))", "010101")
# print(result)
