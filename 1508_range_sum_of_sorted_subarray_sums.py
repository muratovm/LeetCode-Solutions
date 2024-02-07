class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        prefix_sums = [0]
        mod = 10**9 + 7
        for num in nums:
            prefix_sums.append((prefix_sums[-1] + num) % mod)

        sums = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sums.append((prefix_sums[j+1] - prefix_sums[i]))
        sums.sort()
        return sum(sums[left-1:right]) % mod
