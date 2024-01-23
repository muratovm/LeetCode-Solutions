class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        first, second = 1, 1
        for i in range(2, n):
            first, second = second, first+second
        return second
