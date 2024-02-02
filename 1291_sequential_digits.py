class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        source = ["1","2","3","4","5","6","7","8","9"]

        start_length = len(str(low))
        end_length = len(str(high))

        start_low_digit = str(low)[0]
        start_high_digit = str(high)[0]

        length = start_length
        
        i = source.index(start_low_digit)
        results = []
        while length <= end_length:
            if i+length > len(source):
                i = 0
                length += 1
                if i+length > len(source) or length > end_length: break

            result = int("".join(source[i:i+length]))


            if result>=low and result <= high:
                results.append(result)
                
            elif result > high: break
            
            i+=1
        return results
