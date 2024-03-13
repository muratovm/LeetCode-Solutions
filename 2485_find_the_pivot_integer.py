class Solution:
    def pivotInteger(self, n: int) -> int:
        left_prefix = [0]
        right_prefix = [0]
        
        for i in range(1,n+1):
            left_prefix.append(left_prefix[-1]+i)
            
        for i in range(n,0,-1):
            right_prefix.append(right_prefix[-1]+i)
            
        for i in range(1,n+1):
            if left_prefix[i] == right_prefix[n+1-i]:
                return i
        return -1
