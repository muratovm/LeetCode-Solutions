class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        curr_h, curr_min = int(current[:2]), int(current[3:])
        cor_h, cor_min = int(correct[:2]), int(correct[3:])

        h_diff = cor_h - curr_h
        min_diff = cor_min - curr_min

        if min_diff < 0:
            h_diff -= 1
            min_diff += 60

        total = h_diff
        if min_diff >= 15:
            multiplier = min_diff // 15
            total += multiplier
            min_diff -= multiplier*15
        if min_diff >= 5:
            multiplier = min_diff // 5
            total += multiplier
            min_diff -= multiplier*5
        total += min_diff

        return total
