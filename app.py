from flask import Flask, render_template, request
import joblib

# Create Flask application
app = Flask(__name__)

# Load the trained ML model
model = joblib.load("model.pkl")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the HTML form
    so2 = float(request.form["so2"])
    no2 = float(request.form["no2"])
    rspm = float(request.form["rspm"])

    # Make prediction
    prediction = model.predict([[so2, no2, rspm]])

    # Convert prediction to a normal number
    predicted_aqi = round(prediction[0], 2)

    # Send prediction back to HTML
    return render_template(
        "index.html",
        prediction=predicted_aqi
    )


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)