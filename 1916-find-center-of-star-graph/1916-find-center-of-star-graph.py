class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Fetch values from the first two edges
        a, b = edges[0]
        c, d = edges[1]

        # Check if the there are common coordinates in the edges.
        if a == c or a == d:
            return a
        # If a is not equal to any of the coordinates of second edge,
        # then b must be.
        return b
        
        