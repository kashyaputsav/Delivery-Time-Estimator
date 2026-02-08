from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "model.pkl")
model = joblib.load(model_path)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        data = {
            "total_items": float(request.form["total_items"]),
            "subtotal": float(request.form["subtotal"]),
            "num_distinct_items": float(request.form["num_distinct_items"]),
            "min_item_price": float(request.form["min_item_price"]),
            "max_item_price": float(request.form["max_item_price"]),
            "total_onshift_partners": float(request.form["total_onshift_partners"]),
            "total_busy_partners": float(request.form["total_busy_partners"]),
            "total_outstanding_orders": float(request.form["total_outstanding_orders"]),
        }

        # feature engineering
        data["order_size"] = data["total_items"] / max(data["num_distinct_items"], 1)
        data["partner_load"] = data["total_busy_partners"] / max(data["total_onshift_partners"], 1)

        df = pd.DataFrame([data])
        prediction = round(model.predict(df)[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run()


