class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = []
            res = 1  
            for j in range(i+1): 
                row.append(res)
                res = res * (i - j) // (j + 1) 
            triangle.append(row)
        return triangle