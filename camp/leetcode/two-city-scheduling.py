class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for row in costs:
            row.append(row[0]- row[1])

        sortAA= sorted(costs, key= lambda row: row[2])

        minCost, leng= 0, len(costs)
        for i, row in enumerate(sortAA):
            if i< leng/2 :
                minCost += row[0]
            else:
                minCost += row[1]
        
        return minCost
            
        