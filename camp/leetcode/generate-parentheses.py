class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def back_track(opening_count, closing_count, curr):
            
            if opening_count == closing_count == n:
                result.append(''.join(curr))
                
            if opening_count < n:                
                curr.append('(')
                back_track(opening_count + 1, closing_count, curr)
                curr.pop()
                
            if closing_count < opening_count:
                curr.append(')')
                back_track(opening_count, closing_count + 1, curr)
                curr.pop()
                
        back_track(0, 0, [])   
        
        return result
        
                            
                