import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "internal_marks": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
    "result": [
        "Fail", "Fail", "Fail", "Fail", "Pass",
        "Pass", "Pass", "Pass", "Pass", "Pass"
    ]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "internal_marks"]]
y = df["result"]

model = DecisionTreeClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")