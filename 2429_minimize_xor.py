class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        #max supported integer length
        max_binary = 32

        #binary string
        b_num1 = "{0:b}".format(num1)
        b_num2 = "{0:b}".format(num2)

        #binary string of length 32
        b_num1 = "0"*(max_binary-len(b_num1)) + b_num1
        b_num2 = "0"*(max_binary-len(b_num2)) + b_num2

        #find number of set bits for num2
        set_bits = b_num2.count("1")
S
        print(f"Number of bits required: {set_bits}")
        print(f"Number to get close to: {num1}")
        print(f"Bits to get close to: {b_num1}")
       
        result = []

        #set all the same bits as in number 1
        for i in range(max_binary):
            if b_num1[i] == "1" and set_bits > 0:
                result += "1"
                set_bits -= 1
            else:
                result += "0"

        approximation = "".join(result)
        print(f"First Approximation: {approximation}")
        print(f"Bits remaining: {set_bits}")

        #if we have less bits than num2, seed more starting from the end
        if set_bits > 0:
            for i in range(max_binary-1,-1,-1):
                if result[i] == "0":
                    result[i] = "1"
                    set_bits -= 1

                if set_bits == 0:
                    break
            
            #result with the extra 1s
            second_approximation = "".join(result)
            print(f"Additional 1s inserted: {second_approximation}")
        
        #convert to integer and return
        result_int = int("".join(result), 2)
        return result_int
