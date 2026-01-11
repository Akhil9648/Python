from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("house_price_model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        location = data["location"]
        total_sqft = float(data["total_sqft"])
        bath = float(data["bath"])
        bhk = int(data["bhk"])
        price_per_sqft = float(data["price_per_sqft"])

        import pandas as pd

        # Create DataFrame with EXACT same column names as training
        input_df = pd.DataFrame([{
            "location": location,
            "total_sqft": total_sqft,
            "bath": bath,
            "bhk": bhk,
            "price_per_sqft": price_per_sqft
        }])

        prediction = model.predict(input_df)[0]

        return jsonify({
            "prediction": round(float(prediction), 2)
        })

    except Exception as e:
        print("PREDICTION ERROR:", e)
        return jsonify({
            "error": str(e)
        }), 500



if __name__ == "__main__":
    app.run(debug=True, port=5000)
