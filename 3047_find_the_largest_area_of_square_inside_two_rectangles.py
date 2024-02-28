class Solution:
    
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        def intersection(bottom_left_1, top_right_1, bottom_left_2, top_right_2):
            # Calculate the coordinates of the intersection rectangle
            intersection_bottom_left = (max(bottom_left_1[0], bottom_left_2[0]), max(bottom_left_1[1], bottom_left_2[1]))
            intersection_top_right = (min(top_right_1[0], top_right_2[0]), min(top_right_1[1], top_right_2[1]))

            # Check if there is a valid intersection
            if intersection_bottom_left[0] < intersection_top_right[0] and intersection_bottom_left[1] < intersection_top_right[1]:
                return intersection_bottom_left, intersection_top_right
            else:
                return None  # No intersection
            
        biggest_side = 0
        for i in range(len(bottomLeft)):
            for j in range(i+1, len(topRight)):
                space = intersection(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])
                if space:
                    side_length = min(space[1][0] - space[0][0], space[1][1] - space[0][1])
                    biggest_side = max(biggest_side, side_length)
                
        
        return biggest_side**2
