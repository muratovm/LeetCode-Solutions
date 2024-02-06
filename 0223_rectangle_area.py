class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1)*(ay2 - ay1)
        area2 = (bx2 - bx1)*(by2 - by1)

        new_x_range = (max(bx1,ax1), min(bx2,ax2))
        new_y_range = (max(ay1,by1), min(ay2,by2))

        if new_x_range[0] > new_x_range[1] or new_y_range[0] > new_y_range[1]:
            intersection = 0
        else:
            intersection = (new_x_range[1] - new_x_range[0]) * (new_y_range[1] - new_y_range[0])
        
        return area1 + area2 - intersection
