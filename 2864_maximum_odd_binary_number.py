from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = Counter(s)
        ones = counter["1"]
        zeros = len(s)-ones
        return "1"*(ones-1)+"0"*(zeros)+"1"
