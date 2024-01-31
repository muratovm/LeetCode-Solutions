import numpy as np

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        length = len(temperatures)
        output = np.zeros((length), dtype=int)
        stack = []  # This will store indices, not temperatures

        for i in range(length):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                output[prev_index] = i - prev_index
            stack.append(i)

        return output
