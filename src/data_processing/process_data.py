import pandas as pd

class ChurnDataTransformer:
    
    def __init__(self, config = {}):
        self.config = config

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        _df = convert_value(df)
        _df = select_feature(_df)
        _df = ignore_null(_df)
        _df = astype_data(_df)
        return _df

def astype_data(_df):
    _df = _df.astype("Float32", errors="ignore")
    return _df

def ignore_null(_df):
    # check for empty strings in all columns
    is_empty_string = _df.applymap(lambda x: isinstance(x, str) and x.strip() == "")

    # drop rows with empty strings
    _df = _df[~is_empty_string.any(axis=1)]
    return _df


def select_feature(_df):
    features_columns = ["gender", "Partner", "Dependents", "MonthlyCharges", "TotalCharges", "Churn"]
    return _df[features_columns]

    
def convert_value(_df):
    _df["gender"] = _df.apply(lambda x:  0 if x.gender == "Female" else 1, axis = 1)
    _df["Partner"] = _df.apply(lambda x:  0 if x.Partner == "Yes" else 1, axis = 1)
    _df["Dependents"] = _df.apply(lambda x:  0 if x.Dependents == "Yes" else 1, axis = 1)
    _df["Churn"] = _df.apply(lambda x:  0 if x.Churn == "Yes" else 1, axis = 1)
    return _df
       
def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False
