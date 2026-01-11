# model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    df = pd.read_csv("synthetic_data.csv")
    X = df.drop("outcome", axis=1)
    y = df["outcome"]
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model
