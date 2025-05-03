class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = n / time
        step = n % time
        if direction % 2 == 0:
            