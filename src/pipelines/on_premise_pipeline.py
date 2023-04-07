import os

# TRACKING
from src.modeling.custom.model import SklearnModelWrapper
from mlflow.models import infer_signature
import mlflow

from sklearn.model_selection import train_test_split

class Trainer:
    def __init__(self):
        pass
    
    def train(self, model, scorer, x_train, y_train, x_val=None, y_val=None, params={}, experiment_name = "default-name"):
        # Get expierment id
        experiment = get_experiment(experiment_name)
        
        # The run name is an optional argument to `run.init()`
        with mlflow.start_run(experiment_id=experiment.experiment_id) as run:
            # Define values for the parameters to log            
            mlflow.log_params(params)

            # Train locally
            model.fit(
                x_train, 
                y_train
            )
            # print(x_train)
            # print(type(y_train[0]))
            # print(type(model.predict(x_train)[0]))
            # Log metric train metrics
            train_score_results = scorer.score(model.predict(x_train), y_train)
            log_metrics(
                results_score = train_score_results, 
                prefix = "train_")

            # Log metric valid metrics
            valid_score_results = scorer.score(model.predict(x_val), y_val)
            log_metrics(
                        results_score = valid_score_results, 
                        prefix = "val_")
            
        
            # Mlflow log dict
            mlflow.log_dict({"features_columns": x_train.columns.tolist()}, "feature_metadata.json")

            # Log Feature Inportance:
            # mlflow.log_dict({"features_columns": x_train.columns, "label_colum": y_train.columns}, "feature_metadata.json")
            
            # Log model
            input_sample = x_train
            output_model = model.predict(x_train)
            wrappedModel = SklearnModelWrapper(model=model)
            signature = infer_signature(input_sample, output_model)

            mlflow.pyfunc.log_model(
                python_model = wrappedModel,
                artifact_path="model",
                signature =signature)
            
            # Log Tag
            mlflow.set_tag("commit_sha", os.getenv("COMMIT_SHA"))

            return model
        

        
        


def log_metrics(results_score, prefix = None):
    # Define metrics to log
    for rs in results_score:
        _name = rs[0]
        if prefix != None:
            _name = prefix + rs[0]
        mlflow.log_metric(_name,  rs[1])
        
def get_experiment(experiment_name:  str):
    
        """
        Set MLflow experiment.
        """
    
        uri= os.getenv("MLFLOW_TRACKING_URI")
        if uri == None:
            raise Exception("MLFLOW_TRACKING_URI not found in OS")
        
        mlflow.set_tracking_uri(uri)
        experiment_id = mlflow.set_experiment(experiment_name=experiment_name)
        return experiment_id
            
def prepare_training_data(data_loader, data_transformer, label_name, features_name = "*", ignore_columns = None, random_state = 123):
    
    df_data = data_loader.load_data()
    df_data = data_transformer.transform(df_data)
    
    y = df_data[label_name]
    
    if ignore_columns != None:
        if type(ignore_columns) == str:
            df_data.drop(columns=[ignore_columns], inplace = True)
        elif type(ignore_columns) == list:
            df_data.drop(columns=ignore_columns, inplace = True)
    
    X = df_data
    if label_name in df_data.columns:
        X = df_data.drop(columns=[label_name])
        
    #  get feature columns
    if features_name != "*":
        X = X[features_name]
  
    # Split dataset
    X_train , X_val, y_train, y_val = train_test_split(X, y, random_state = random_state)
    return X_train , X_val, y_train, y_val
        

if __name__ == "__main__":
    from tqdm import tqdm
    from src.modeling.custom.model import CatboostCustomClassifier
    from src.modeling.custom.score import MLScorer
    from src.data_processing.load_data import DataLoader
    from src.data_processing.process_data import ChurnDataTransformer
    from src.utils.ml_utils import generate_params
    import warnings


    warnings.filterwarnings("ignore")
    
    LABEL_COLUMN = "Churn"
    FEATURE_COLUMNS = "*"
    LOCATION_PATH = "datasets/raw_datas/churn_dataset_train.csv"
    GRID_VALUES = {'iterations': [100, 200, 500, 1000], 'learning_rate':[0.001,.003], 'depth': [5, 10]}
    
    scorer = MLScorer()
    trainer = Trainer()
    dataloader = DataLoader(LOCATION_PATH)
    data_tranformer = ChurnDataTransformer()

    X_train, X_val, y_train, y_val = prepare_training_data(
        data_loader=dataloader,  
        data_transformer=data_tranformer,
        label_name=LABEL_COLUMN, 
        features_name=FEATURE_COLUMNS)

    for params in tqdm(generate_params(GRID_VALUES)):
        model_catboost = CatboostCustomClassifier(model_params = params)
        model_trained = trainer.train(
                        model = model_catboost, 
                        scorer = scorer, 
                        x_train = X_train, 
                        y_train =y_train, 
                        x_val=X_val, 
                        y_val=y_val, 
                        params=params, 
                        experiment_name=os.getenv("MLFLOW_EXPERIMENT_NAME", "defaults"))
