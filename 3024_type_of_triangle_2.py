from collections import Counter

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        #is triangle
        side_1 = (nums[0] + nums[1]) > nums[2]
        side_2 = (nums[1] + nums[2]) > nums[0]
        side_3 = (nums[2] + nums[0]) > nums[1]
        
        if side_1 and side_2 and side_3:
            counter = Counter(nums)
            for key in counter:
                if counter[key] == 3:
                    return "equilateral"
                if counter[key] == 2:
                    return "isosceles"
            return "scalene"
        else:
            return "none"
