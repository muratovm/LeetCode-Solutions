class Solution:
    def reverseVowels(self, s: str) -> str:
        backward_vowels = list(filter(lambda i: s[i] in {"a","e", "i", "o", "u", "A","E","I","O","U"}, range(len(s)-1,-1,-1)))
        if len(backward_vowels) == 0:
            return s
        
        string = ""
        j = 0
        k = len(backward_vowels)-1
        for i in range(len(s)):
            if i == backward_vowels[k]:
                string += s[backward_vowels[j]]
                j+=1
                k-=1
            else:
                string += s[i]
        return string
