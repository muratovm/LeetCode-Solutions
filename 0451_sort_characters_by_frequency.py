from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        result = ""
        for char in sorted(counter, key=lambda x: counter[x], reverse=True):
            result += char*counter[char]
        return result
