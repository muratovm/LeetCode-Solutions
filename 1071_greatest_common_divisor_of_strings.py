class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str_1 = len(str1)
        len_str_2 = len(str2)
        smallest = min(len_str_1,len_str_2)
        for i in range(smallest,-1,-1):
            prefix_len = i+1
            if len_str_1 % prefix_len == 0 and len_str_2 % prefix_len == 0:
                prefix = str1[:prefix_len]
                multiple_1 = len_str_1 // prefix_len
                multiple_2 = len_str_2 // prefix_len
                if prefix * multiple_1 == str1 and prefix * multiple_2 == str2:
                    return prefix
        return ""
