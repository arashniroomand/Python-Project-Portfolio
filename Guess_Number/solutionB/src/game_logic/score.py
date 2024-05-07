class Score:
    def __init__(self,inital_score = 100):
        self.score = inital_score
    
    def decrement_state(self,penalty = 10):
        """decrease the score and return it"""
        self.score -= penalty
        self.score = max(self.score,0)
    
    def get_score(self):
        """show the result"""
        return self.score
        