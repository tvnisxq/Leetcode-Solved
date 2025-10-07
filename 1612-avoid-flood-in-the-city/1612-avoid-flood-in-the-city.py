import bisect
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res, full, dry = [1] * n, {}, SortedList()

        for i, lake in enumerate(rains):
            if lake == 0:
                dry.add(i) 
                res[i] = 1

            elif lake in full:
                res[i] = -1
                j = dry.bisect_right(full[lake])
                
                if j == len(dry):
                    return []
                
                res [dry[j]] = lake
                dry.pop(j)
                full[lake] = i
            
            else:
                full[lake] = i
                res[i] = -1

        return res   