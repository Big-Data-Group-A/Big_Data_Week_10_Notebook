Week 10 Lab: Machine Learning & Dashboards

Course: INSY 8413 Introduction to Big Data Analytics, AUCA Instructor: Prince Ishimwe Student: Mucyo Gad

About this project

This project predicts a student's final score from their quiz average, assignments average and attendance. It also identifies students at risk of failing and shares the findings in a simple interactive dashboard.

What it does
Explore and split: loads the data, checks correlations, and splits it into 112 training and 38 test students (test_size=0.25, random_state=42).
Regression: a linear regression predicts the score.
Classification: a logistic regression predicts pass or fail (score of 50 or more), and the confusion matrix is compared with a "predict pass for everyone" baseline.
Feature engineering: compares three versions of the regression, including one-hot encoded program.
Dashboard: three Plotly charts, with the at-risk scatter saved as class_dashboard.html.
Bonus: a box plot of scores by program.
Files
File	Description
Week10_Mucyo_Gad.ipynb	The completed notebook (code and outputs)
week10_students.csv	The dataset: 150 students, 9 columns
class_dashboard.html	The interactive "Who is at risk" scatter chart
Week10_Lab_Outputs_Mucyo_Gad.pdf	Code and output for every part
Week10_Lab_Report_Mucyo_Gad.pdf	Written lab report with the model card
Dataset columns

student_id, name, gender, program, district, attendance_pct, quiz_avg, assignments_avg, score (the target).

Requirements
Python 3
pandas
numpy
scikit-learn
plotly

Google Colab already has everything installed. On Anaconda, run pip install plotly if the import fails.

How to run
Open the notebook in Google Colab (File, then Upload notebook) or in Jupyter.
Upload week10_students.csv next to the notebook (Colab: folder icon on the left, then the upload icon).
Click Runtime, then Run all.
class_dashboard.html is saved next to the notebook. Open it in a browser and hover over the points to see student names.
Results
Measure	Value
Regression MAE (test set)	3.33 points
Regression R² (test set)	0.89
Classification accuracy	0.895 (same as the lazy baseline)
Failing students correctly flagged	3 of 4
R² with quiz only / three features / plus program	0.62 / 0.89 / 0.88

Quiz average is the strongest predictor (correlation 0.80 with score). One extra quiz point adds about 0.58 points to the predicted score.

Model card (short)
Purpose: predicts a student's final score to help lecturers offer early support.
Performance: off by about 3 points on average on unseen students.
Use it to: start a conversation and offer support early.
Do not use it to: decide grades, pass/fail, scholarships or discipline. It sees only three numbers and was trained on 150 students from one course.
