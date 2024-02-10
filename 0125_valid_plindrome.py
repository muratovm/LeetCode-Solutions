class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = "".join(list(filter(lambda s: s.islower() or s.isnumeric(), s.lower())))
        return palindrome == palindrome[::-1]
