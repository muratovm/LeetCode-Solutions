import numpy as np

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0: return 0
        expanded_field = np.zeros((m+2, n+2), dtype=int)
        
        def in_bounds(x,y): return (0<=x<=n+1) and (0<=y<=m+1)
        def on_border(x,y): return x == 0 or x == n+1 or y == 0 or y == m+1
        def get_neighbors(x,y): 
            options = []
            if x-1 > 0:
                options.append((x-1,y))
            if y-1 > 0:
                options.append((x,y-1))
            if x <= n:
                options.append((x+1,y))
            if y <= m:
                options.append((x,y+1))
            return options
        
        
        #set the surounding squares to 1 for the first move
        expanded_field[startRow+1][startColumn] = 1
        expanded_field[startRow][startColumn+1] = 1
        expanded_field[startRow+1][startColumn+2] = 1
        expanded_field[startRow+2][startColumn+1] = 1
        
        
        def add_neighbours(field):
            new_field = np.zeros((m+2, n+2), dtype=int)
            for y in range(len(new_field)):
                for x in range(len(new_field[0])):
                    #save the previous outbounds
                    if on_border(x,y):
                        new_field[y][x] = field[y][x]
                        
                    #calculate paths inside the field
                    for n_x,n_y in get_neighbors(x,y):
                        if not on_border(n_x,n_y):
                            new_field[y][x] = (new_field[y][x] + field[n_y][n_x])  % (10**9 + 7)
            return new_field
                            
        #print(expanded_field)
        for i in range(maxMove-1):
            #print("===================")
            expanded_field = add_neighbours(expanded_field)
            #print(expanded_field)
            
        top =sum(expanded_field[0]) % (10**9 + 7)
        bottom = sum(expanded_field[-1]) % (10**9 + 7)
        left = sum(expanded_field[:,0]) % (10**9 + 7)
        right = sum(expanded_field[:,-1]) % (10**9 + 7)
        
        return (top + bottom + left + right) % (10**9 + 7)
