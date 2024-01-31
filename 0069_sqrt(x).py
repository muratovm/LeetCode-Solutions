import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x in [1,2,3]: return 1
        start = 0
        end = x//2
        while start <= end:
            mid = (end+start)//2
            result = mid * mid
            if result == x: return mid
            elif result < x: start=mid+1
            else: end = mid-1
        return end
