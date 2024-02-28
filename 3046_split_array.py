from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        most = counter.most_common(1)
        return most[0][1] <= 2
