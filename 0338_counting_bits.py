class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1,n+1):
            if i%2 == 1:
                result.append(result[-1]+1)
            else:
                result.append(result[i>>1])
        return result
