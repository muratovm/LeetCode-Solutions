from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        total = sum(nums)
        most_common = Counter(nums).most_common(1)[0][0]
        
        if length % 2 == 0:
            expected = (length + 1) * (length //2)
        else:
            expected = (length + 2) * (length //2) + 1
    
        diff = expected - total        
        return [most_common, most_common+diff]
