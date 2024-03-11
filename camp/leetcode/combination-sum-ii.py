class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            def backtrack(i, path, total):
                if total == target:
                    res.append(path[:])
                    return 
                if i >= len(candidates) or total > target:
                    return
                
                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])
                path.pop()
                
                while i< len(candidates)-1 and candidates[i] == candidates[i+1]:
                    i = i + 1
                backtrack(i+1, path, total)
                    
            candidates.sort() 
            res = []
            backtrack(0, [], 0)
            return res