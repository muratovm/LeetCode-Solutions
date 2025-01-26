import math

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def isSafe(index):

            #already visited, we are in a loop      :Not Safe
            if state[index] == 1: 
                return False
            
            #base case, termination node            :Safe
            if graph[index] == [] or state[index] == 2:
                state[index] = 2
                return True
            
            #mark node as visited
            state[index] = 1
            for option in graph[index]:
                #if any option is unsafe, this node is unsafe
                if not isSafe(option): 
                    return False
            
            #mark node as safe
            state[index] = 2
            return True


        result = []
        #everything unvisited will be a 0
        state = defaultdict(lambda : 0)

        for i, val in enumerate(graph):
            if isSafe(i):
                result.append(i)
        return result