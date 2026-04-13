import pytest
import pandas as pd
from pathlib import Path
from cleaning import load_data, clean_data, encoding, split_data

@pytest.fixture(scope="session")
def df_sample():
    df = load_data("data/Test_df.csv")
    return df

@pytest.fixture(scope="session")
def df_processed(df_sample):
    df = clean_data(df_sample)
    df = encoding(df)
    return df

@pytest.fixture(scope="session")
def splits(df_processed):
    X_train, X_test, y_train, y_test = split_data(df_processed)
    return X_train, X_test, y_train, y_test