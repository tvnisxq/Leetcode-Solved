class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Time: O(n²)
        Space: O(n)
        """
        result = [[1]]

        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            result.append(row)
        return result

