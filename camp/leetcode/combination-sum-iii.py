class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # k is size of list, n is target
        arr =[i for i in range(1, 10)]
        res =[]
        def dfs(i, cur, total):
            if len(cur) ==k and total ==n:
                res.append(cur.copy())
                return
            if i >= 9 or total >n or len(cur)>=k:
                return

            cur.append(arr[i])
            dfs(i+1, cur, total +arr[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res