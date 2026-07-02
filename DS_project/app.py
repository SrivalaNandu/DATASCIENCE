from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model/student_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    gender = request.form["gender"]
    race = request.form["race"]
    parent = request.form["parent"]
    lunch = request.form["lunch"]
    preparation = request.form["preparation"]
    reading = int(request.form["reading"])
    writing = int(request.form["writing"])

    data = pd.DataFrame({
        "gender":[gender],
        "race/ethnicity":[race],
        "parental level of education":[parent],
        "lunch":[lunch],
        "test preparation course":[preparation],
        "reading score":[reading],
        "writing score":[writing]
    })

    prediction = model.predict(data)[0]

    return render_template(
        "result.html",
        prediction=round(prediction,2)
    )

if __name__ == "__main__":
    app.run(debug=True)