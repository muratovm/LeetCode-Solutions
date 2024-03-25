class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums)):
            
            element = abs(nums[i])-1
            if nums[element] < 0:
                result.append(element+1)
            else:
                nums[element] = -nums[element]

        return result
