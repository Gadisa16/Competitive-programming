class Solution:
    def deckRevealedIncreasing(self, deck):
        res = []
    
        for card in sorted(deck,reverse=True):
            if res:
                temp = res.pop()
                res.insert(0, temp)
            res.insert(0, card)
        
        return res