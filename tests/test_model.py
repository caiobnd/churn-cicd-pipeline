import pytest
from pathlib import Path
from sklearn.metrics import recall_score
from model import train_logistic_regression

RECALL_THRESHOLD = 0.70

def test_model_file_exists():
    assert Path("model/logisticregression.pkl").exists()

def test_model_recall(splits):
    X_train, X_test, y_train, y_test = splits
    model = train_logistic_regression(X_train, y_train)
    y_pred = model.predict(X_test)
    recall = recall_score(y_test, y_pred)
    assert recall > RECALL_THRESHOLD, f"Recall {recall:.2f} abaixo do threshold {RECALL_THRESHOLD}"