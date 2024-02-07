from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return "".join(char*counter[char] for char in sorted(counter, key=lambda x: counter[x], reverse=True))
