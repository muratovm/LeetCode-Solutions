class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = "".join([a+b for a,b in zip(word1,word2)])
        diff = len(word2) - len(word1)
        if diff > 0:
            merge+= word2[len(word1):]
        elif diff < 0:
            merge+= word1[len(word2):]
        return merge
