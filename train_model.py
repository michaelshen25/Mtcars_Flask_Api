import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("mtcars.csv", index_col=0)

X = df.drop(columns=["mpg"])
y = df["mpg"]

model = LinearRegression().fit(X, y)

joblib.dump(model, "model.pkl")
