class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1,set_2 = set(nums1),set(nums2)
        return [set_1-set_2, set_2-set_1]
