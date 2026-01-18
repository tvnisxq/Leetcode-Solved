class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to the prereq list
        preMap = {i:[] for i  in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # VisitSet = all courses along the current DFS path
        visitSet = set()

        # dfs function for traversal
        def dfs(crs):
            # Base case
            if crs in visitSet:
                return False # already visited
            if preMap[crs] == []:
                return True # Completed the prerequisite
            
            # Other case is where we complete the current course 
            # so we add it to the visitSet
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs) # Remove the course(since completed) for next dfs traversals
            preMap[crs] = [] # Also make the preMap of this course empty
            return True

        # Iteratively calling the function: for what if the graph is not connected
        # so we need to iterate over every single course
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True