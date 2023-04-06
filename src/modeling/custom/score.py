from sklearn.metrics import accuracy_score

class MLScorer:
    def __init__(self):
        pass
    
    def score(self, predicts, targets):
        result_scores = []
        result_scores.append(("accuracy", accuracy_score(predicts, targets)))
        #TODO APPEND MORE OTHER METRICS
    
        return result_scores
        
        