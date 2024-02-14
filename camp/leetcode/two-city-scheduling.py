class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for row in costs:
            row.append(row[1]- row[0])

        sortAA= sorted(costs, key= lambda row: row[2], reverse= True)

        minCost, leng= 0, len(costs)
        for i, row in enumerate(sortAA):
            if i< leng/2 :
                minCost += row[0]
            else:
                minCost += row[1]
        
        return minCost
            
        