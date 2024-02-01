class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        char_to_int = {"1": 1, "2": 2, "3": 3,
                   "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9, "0":0}
        
        def my_int(string):
            total, base = 0,0
            for i in range(len(string)-1,-1,-1):
                total += char_to_int[string[i]] * (10**base)
                base += 1
            return total
        
        return str(my_int(num1) * my_int(num2))
