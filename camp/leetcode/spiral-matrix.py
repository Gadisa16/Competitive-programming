class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        T, B, L, R, dir = 0, len(A) - 1, 0, len(A[0]) - 1, 0
        ans = []

        while T <= B and L <= R:
            if dir == 0:
                for i in range(L, R + 1):
                    ans.append(A[T][i])
                T += 1
            elif dir == 1:
                for i in range(T, B + 1):
                    ans.append(A[i][R])
                R -= 1
            elif dir == 2:
                for i in range(R, L - 1, -1):
                    ans.append(A[B][i])
                B -= 1
            elif dir == 3:
                for i in range(B, T - 1, -1):
                    ans.append(A[i][L])
                L += 1
            dir = (dir + 1) % 4

        return ans
