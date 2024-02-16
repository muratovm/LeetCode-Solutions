class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros_seen = 1
        for i in range(len(flowerbed)):

            #accumulate zeros seen
            if flowerbed[i] == 0: zeros_seen += 1
            else: zeros_seen = 0

            #if 3 zeros seen, reset zeros to 1, decrement n
            if zeros_seen == 3: zeros_seen, n = 1, n-1
            
            #early termination
            if n <= 0: return True

        #if we've seen 2 seros and we're at the end of the list, assume implicit ending 0
        if zeros_seen == 2: return n <= 1

        #didn't terminate early, so we didn't palce all 1s
        return False
