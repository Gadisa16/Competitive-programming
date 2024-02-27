class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex - 1)
        currentRow = [1]
        for i in range(len(prevRow) - 1):
            currentRow.append(prevRow[i] + prevRow[i + 1])
        currentRow.append(1)
        return currentRow