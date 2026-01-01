import pickle

# Load trained model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Enter Student Details")

attendance = float(input("Attendance %: "))
internal = float(input("Internal Marks: "))
assignment = float(input("Assignment Marks: "))
lab = float(input("Lab Performance Marks: "))

# Predict
prediction = model.predict([[attendance, internal, assignment, lab]])

if prediction[0] == 1:
    print("Prediction Result: PASS ✅")
else:
    print("Prediction Result: FAIL ❌")