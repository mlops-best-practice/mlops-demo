import pandas as pd

class ChurnDataTransformer:
    
    def __init__(self, config = {}):
        self.config = config

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        selected_columns = ["gender", "Partner", "Dependents", "MonthlyCharges", "TotalCharges", "Churn"]
        _df = df.drop("customerID", axis=1)
        _df["gender"] = _df.apply(lambda x:  0 if x.gender == "Female" else 1, axis = 1)
        _df["Partner"] = _df.apply(lambda x:  0 if x.Partner == "Yes" else 1, axis = 1)
        _df["Dependents"] = _df.apply(lambda x:  0 if x.Dependents == "Yes" else 1, axis = 1)
        _df["Churn"] = _df.apply(lambda x:  0 if x.Churn == "Yes" else 1, axis = 1)
        df_selected = _df[selected_columns]
        return df_selected

       
