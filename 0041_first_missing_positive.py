class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Remove duplicates and sort the list to prepare for finding the smallest missing positive
        nums = sorted(list(set(nums)))

        # Initialize the search for the smallest missing positive integer
        smallest = 1
        previous = 0

        for num in nums:
            if num <= 0: # Ignore non-positive numbers
                continue

            if num == smallest: # Move to the next expected smallest positive integer
                smallest += 1
                previous = num

            else:
                # If there's a gap in the sequence, return the first missing integer
                return previous + 1

        # If the sequence is unbroken but ends before covering all positive integers,
        # return the next expected positive integer. If the list was all non-positive,
        # default to returning 1.
        return max(nums[-1]+1, 1)
