class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_elevations = [0]
        for change in gain:
            current_elevations.append(current_elevations[-1]+change)
        return max(current_elevations)
