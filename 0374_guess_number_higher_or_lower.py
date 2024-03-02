# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end, prediction = 0, n, n//2
        result = None

        while result != 0:
            result = guess(prediction)
            if result == 1:
                start, end = prediction+1, end
            elif result == -1:
                start, end = start, prediction-1

            prediction = (end + start) // 2

        return prediction
