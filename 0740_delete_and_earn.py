from collections import Counter

class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        counter = Counter(nums)
        unique_nums = sorted(counter)
        totals = [num * counter[num] for num in unique_nums]
        prev = None
        last, second_last, third_last = 0,0,0
        for i in range(len(unique_nums)):
            if unique_nums[i]-1 == prev:
                totals[i] += max(second_last, third_last) 
            else:
                totals[i] += max(last, second_last)
            prev = unique_nums[i]
            last, second_last, third_last = totals[i], last, second_last
            
        return max(last,second_last,third_last)
