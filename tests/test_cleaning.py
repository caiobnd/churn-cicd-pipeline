import pandas   as    pd
import numpy    as    np
import pytest
from cleaning   import clean_data, encoding, split_data,load_data
from constants  import binary_columns


def test_clean(df_sample):
    
    df_test = clean_data(df_sample)
    
    assert df_test["TotalCharges"].notna().all()
    assert "customer" not in df_test.columns
    
def test_enconding(df_processed):
    
    df = df_processed
    
    bool_columns = df.select_dtypes(include=['bool']).columns
    
    assert "No internet service" not in df.values
    assert "Male" not in df.values and "Female" not in df.values
    assert "Yes"  not in df.values and "No" not in df.values
    assert len(bool_columns) == 0
    
def test_split(splits,df_processed):
    
    X_train, X_test, y_train, y_test    = splits
    df                                  = df_processed
    
    assert "Churn" not in X_train.columns
    assert "Churn" not in X_test.columns
    assert df[binary_columns].dtypes.eq(int).all()
    assert df.select_dtypes(include='object').empty
    assert len(X_train) + len(X_test) == len(df)
    assert X_train.shape[1] == X_test.shape[1]
    