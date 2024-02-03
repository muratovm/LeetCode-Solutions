class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        total = 0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                
                first_point = points[i]
                second_point = points[j]
                
                
                #follows square rule
                
                first_type = first_point[0] >= second_point[0] and first_point[1] <= second_point[1]
                second_type = second_point[0] >= first_point[0] and second_point[1] <= first_point[1]
                
                if first_type:
                    #print(first_point, second_point)
                    #check if any points are inside the boundary
                    inside_any = False
                    for o in range(len(points)):
                        #other point
                        if o != i and o != j:
                            other_point = points[o]
                            
                            first_condition = (second_point[0] <= other_point[0] <= first_point[0])
                            second_condition = (first_point[1] <= other_point[1] <= second_point[1])
                            
                            #print(first_condition, second_condition)
                            if first_condition and second_condition:
                                inside_any = True
                                break
                                
                    #print(inside_any)
                    if not inside_any:
                        total += 1
                            
                if second_type:
                    #print(first_point, second_point)
                    inside_any = False
                    for o in range(len(points)):
                        #other point
                        if o != i and o != j:
                            other_point = points[o]
                            
                            first_condition = (first_point[0] <= other_point[0] <= second_point[0])
                            second_condition = (second_point[1] <= other_point[1] <= first_point[1])
                            
                            #print(first_condition, second_condition)
                            if first_condition and second_condition:
                                inside_any = True
                                break
                                
                    #print(inside_any)    
                    if not inside_any:
                        total += 1
        return total
                            
                            
        
        
