Week 10 Lab: Machine Learning & Dashboards

Course: Introduction to Big Data Analytics, AUCA Instructor: Prince Ishimwe Student: your name · ID: your student ID · Program: your program

Overview

This lab trains, evaluates and publishes machine learning models on a dataset of 150 AUCA students.

Regression: predict a student's final score from quiz average, assignment average and attendance.
Classification: flag at-risk students (score below 50) with logistic regression.
Feature engineering: compare three versions of the regression model.
Dashboard: share the results as interactive Plotly charts.
Files
File	Description
Week10_YourName.ipynb	Completed notebook with all exercises, comments and the model card
week10_students.csv	Dataset: 150 students, 9 columns (converted from the provided .xlsx)
class_dashboard.html	Interactive "2. Who is at risk" scatter plot (open in a browser)
dashboard_screenshot.png	Screenshot of the dashboard open in a browser
model_card.md	Model card for the regression model
README.md	This file
Dataset

week10_students.csv has these columns: student_id, name, gender, program, district, attendance_pct, quiz_avg, assignments_avg, score (the target).

If you only have the Excel file, convert it first:

python
import pandas as pd
pd.read_excel("week10_students.xlsx").to_csv("week10_students.csv", index=False)
How to run
Put Week10_YourName.ipynb and week10_students.csv in the same folder.
Install the libraries if needed: pip install pandas scikit-learn plotly (Colab has them already).
Open the notebook and choose Run all.
The notebook writes class_dashboard.html to the same folder. Open it in a browser.

All splits use test_size=0.25, random_state=42, giving 112 training and 38 test students.

Results
Part	Result
1. Explore	Correlation with score: quiz 0.80, assignments 0.54, attendance 0.24
2. Regression	Test MAE = 3.33 points, R² = 0.887. One extra quiz point ≈ +0.58 exam points
2.3 New student	Quiz 70, assignments 75, attendance 90 → predicted score 73.7
3. Classification	131 pass / 19 fail. Accuracy 0.895 equals the lazy baseline 0.895, but the model catches 3 of the 4 failing students (baseline catches 0). Confusion matrix [[3,1],[3,31]]
4. Feature engineering	Test R²: quiz only 0.624 → three features 0.887 → three + program 0.880
5. Dashboard	Three charts (class scores, at-risk scatter, district averages); the scatter is saved as HTML
Bonus	Networking is the most consistent program; Software Engineering has the widest spread
Key takeaways
Always evaluate on data the model has not seen (the test set).
Accuracy can mislead when classes are imbalanced. Use the confusion matrix, recall and precision.
More features help only when they carry new, relevant information.
Predictions support human decisions, such as early help for students. They must not decide grades or opportunities on their own.
Model card

See model_card.md (also the last cell of the notebook): purpose, data and features, performance on unseen data, and risks.

Submission checklist
 Notebook renamed Week10_YourName with your own name
 Regression evaluated on the test set
 Confusion-matrix argument written
 class_dashboard.html saved, plus a screenshot
 Model card written
 Submitted before the end of Week 10
Tools

Python · pandas · scikit-learn (train_test_split, LinearRegression, LogisticRegression) · Plotly Express · Jupyter
