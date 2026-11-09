# ADVENTIST UNIVERSITY OF CENTRAL AFRICA (AUCA)

## Week 10 Lab — Machine Learning & Dashboards

**Course Name:**  Introduction to Big Data Analytics  
**Student ID:** 29061  
**Student Name:** Mutangana Joseph  

---
# Part 6. Model Card — Student Score Prediction

### 1. Purpose
The model predicts students' final exam scores based on their quiz average, assignment average, and attendance percentage. It can help lecturers and academic staff identify students who may need additional academic support.

### 2. Data & Features
The model was trained using student data containing three input features:
- `quiz_avg` — average quiz score.
- `assignments_avg` — average assignment score.
- `attendance_pct` — student attendance percentage.

The target variable was `score`, representing the student's final exam score.

### 3. Performance
The model was evaluated using unseen test data.

- **MAE: 3.33** — The model's predictions differ from actual student scores by approximately 3.33 points on average.
- **R²: 0.89** — The model reduces squared prediction error by approximately 89% compared with simply predicting the average score for every student.

These results indicate that the model performs well on the test data.

### 4. Risks and Limitations
Incorrect predictions could cause students to be wrongly identified as needing academic support or to be overlooked when they actually need help.

The model should be used as a supporting tool to help lecturers identify students who may need attention. Predictions should be reviewed alongside other academic information and professional judgment.

The model should NOT be used as the sole basis for assigning grades, making academic decisions, or judging a student's ability.