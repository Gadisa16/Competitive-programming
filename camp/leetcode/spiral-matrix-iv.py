# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        T, B, L, R, dir = 0, m - 1, 0, n - 1, 0

        while T <= B and L <= R and head:
            if dir == 0:
                for i in range(L, R + 1):
                    matrix[T][i] = head.val
                    head = head.next
                    if head is None:
                        return matrix
                T +=1

            elif dir == 1:
                for i in range(T, B + 1):
                    matrix[i][R] = head.val
                    head = head.next
                    if head is None:
                        return matrix
                R -=1

            elif dir == 2:
                for i in range(R, L - 1, -1):
                    matrix[B][i] = head.val
                    head = head.next
                    if head is None:
                        return matrix
                B -=1

            elif dir == 3:
                for i in range(B, T - 1, -1):
                    matrix[i][L] = head.val
                    head = head.next
                    if head is None:
                        return matrix
                L +=1
            dir = (dir + 1) % 4

        return matrix
