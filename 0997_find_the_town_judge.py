class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * n
        trusts = set()
        for a,b in trust:
            trusted[b-1] += 1
            trusts.add(a)
        
        if n-1 in trusted:
            index = trusted.index(n-1)+1
            if index in trusts: return -1
            return index

        return -1
