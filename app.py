from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Result Predictor</title>
</head>

<body>

<h1>Student Result Predictor</h1>

<form method="POST">

    <label>Study Hours:</label>
    <input type="number" step="0.1" name="study_hours" required>
    <br><br>

    <label>Attendance %:</label>
    <input type="number" step="0.1" name="attendance" required>
    <br><br>

    <label>Internal Marks:</label>
    <input type="number" step="0.1" name="internal_marks" required>
    <br><br>

    <button type="submit">Predict</button>

</form>

{% if prediction %}
<h2>Prediction: {{ prediction }}</h2>
{% endif %}

<h3>Model Version: 1.0</h3>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        internal_marks = float(request.form["internal_marks"])

        prediction = model.predict([
            [study_hours, attendance, internal_marks]
        ])[0]

    return render_template_string(
        HTML,
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)