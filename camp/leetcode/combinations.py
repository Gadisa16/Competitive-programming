class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans, path =[], []

        def backtrack(first_num):
            print(path)
            if  len(path)==k:
                ans.append(path[:])
                return

            for next_candidate in range(first_num, n+1):                
                    path.append(next_candidate)
                    backtrack(next_candidate +1)#given the candid explore further.                  
                    path.pop() # backtrack
            
        backtrack(1)
        return ans