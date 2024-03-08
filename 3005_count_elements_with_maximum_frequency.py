from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_appearances = counter.most_common(1)[0][1]
        new_list = list(filter(lambda x: counter[x] == max_appearances, counter))
        return max_appearances * len(new_list)
