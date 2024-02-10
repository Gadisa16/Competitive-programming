class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref= [[0 for _ in range(len(matrix[0])+1)] for _ in range((len(matrix)+1))]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.pref[i][j]= self.pref[i-1][j] + self.pref[i][j-1] - self.pref[i-1][j-1] + matrix[i-1][j-1]
        
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1 #c1, r2.. are for matrix but for pref we have shifted by adding 0 column and row
        return self.pref[r2][c2] - self.pref[r2][c1-1] - self.pref[r1-1][c2] +self.pref[r1-1][c1-1]


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)