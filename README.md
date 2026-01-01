# Student-Performance-Prediction
**📌 Project Description**

* This project predicts whether a student will PASS or FAIL using Machine Learning based on academic and performance-related parameters.
* It applies Logistic Regression, a supervised learning algorithm, to analyze student data and provide accurate predictions.
* The goal of this project is to demonstrate the end-to-end Machine Learning workflow — from dataset loading and model training to evaluation and real-time prediction.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**🎯 Project Objective**

* Predict student academic outcomes (Pass / Fail)
* Apply Machine Learning to a real-world education problem
* Understand supervised learning and model evaluation
* Gain hands-on experience with Python and Scikit-learn
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**📊 Dataset**

* The dataset contains student academic records with the following attributes:

* Feature---------> Description
* attendance------> Attendance percentage
* internal--------> Internal exam marks
* assignment------>	Assignment marks
* lab	Lab---------> performance marks
* result----------> Target variable (1 = Pass, 0 = Fail)

**📁 Dataset format: CSV**
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**🛠 Tools & Technologies**

* Language: Python
* Libraries:
* Pandas
* NumPy
* Scikit-learn
* Algorithm: Logistic Regression
* Model Storage: Pickle (.pkl)
* IDE: VS Code / Python CLI
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**🔁 AI / ML Workflow**

* Load and preprocess dataset
* Select relevant features
* Split data into training and testing sets
* Train Logistic Regression model
* Evaluate model using accuracy score
* Save trained model (student_model.pkl)
* Predict results using user input
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**📈 Model Performance**

* The model was evaluated using accuracy score
* Achieved reliable performance for binary classification
* Suitable for small to medium-sized structured datasets

▶️ How to Run the Project
1️⃣ Install Required Libraries
* pip install pandas numpy scikit-learn

2️⃣ Train the Model
* python train_model.py

3️⃣ Run Prediction
* python predict.py

4️⃣ Sample Input
* Attendance %: 85
* Internal Marks: 78
* Assignment Marks: 80
* Lab Performance Marks: 90

5️⃣ Output
* Prediction Result: PASS ✅
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**📂 Project Structure**

* student-performance-prediction/
* │
* ├── dataset.csv
* ├── train_model.py
* ├── predict.py
* ├── student_model.pkl
* └── README.md
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
**🚀 Future Enhancements**

* Add more student features (quiz scores, behavior metrics)
* Improve accuracy using advanced ML algorithms
* Create a web interface using Flask / Streamlit
* Visualize data insights using graphs and charts
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

**🧑‍💻 Author**
  
* Kishore S
* B.Tech – Artificial Intelligence & Data Science
