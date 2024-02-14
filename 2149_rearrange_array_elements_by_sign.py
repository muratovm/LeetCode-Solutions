class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_array = list(filter(lambda x: x>=0 ,nums))
        negatve_array = list(filter(lambda x: x<0 ,nums))
        return [array[i] for i in range(len(positive_array)) for array in [positive_array, negatve_array]]
