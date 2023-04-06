from catboost import CatBoostClassifier
import mlflow

from abc import ABC, abstractmethod

class BaseModelClassifier(ABC):
    @abstractmethod
    def __init__(self, model_params):
        self.model = None   

    @abstractmethod
    def get_requirements(self):
        return NotImplemented

    @abstractmethod
    def fit(self, X, y):
        '''
        fit data into model
        '''
        return NotImplemented
    
    @abstractmethod
    def predict(self, X):
        return NotImplemented
    
    

class CatboostCustomClassifier:
    '''
    Demo catboost classifier custom
    '''
    def __init__(self, model_params):
        self._setup_params(model_params)

    def _setup_params(self, model_params):
        # setup not generate catboost_info file to local
        if "allow_writing_files" not in model_params:
            model_params["allow_writing_files"] = False
        
        # setup not output to stdout
        if "logging_level" not in model_params:
            model_params["logging_level"] = 'Silent'   
        self.model = CatBoostClassifier(**model_params)
    
    def fit(self, X, y):
        '''
        fit data into model
        '''
        # split data to bucketing
        self.model.fit(X, y)
        return self.model
    
    def predict(self, X):
        out_pred = self.model.predict(X)
        return out_pred
    


#function to wrap the pipeline to be logged by mlflow
class SklearnModelWrapper(mlflow.pyfunc.PythonModel):
    def __init__(self, model):
        self.model = model
    def predict(self, context, model_input):
#         _logger.info(self.model.predict(model_input))
        return self.model.predict(model_input)