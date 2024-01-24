class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        greed = sorted(g)
        cookies = sorted(s)
        
        child = 0
        total = 0
        for cookie in cookies:
            if cookie >= greed[child]:
                total += 1
                child += 1
            if child == len(greed):
                break
        return total
