from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    df = pd.DataFrame([payload])
    prediction = model.predict(df)[0]
    return jsonify({"predicted_mpg": float(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
