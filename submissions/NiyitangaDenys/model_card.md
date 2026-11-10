# Model Card — Student Score Prediction

**Student:** Niyitanga Denys  
**Student ID:** 29125  
**Program:** Software Engineering  
**Course:** Introduction to Big Data Analytics — Week 10 Lab

## 1. Purpose
This linear regression model estimates a student's assessment score from their quiz average, assignment average, and attendance percentage. It is intended for educational analysis and early identification of students who may benefit from additional academic support.

## 2. Data and features
The model uses the supplied dataset of **150 students**. The input features are `quiz_avg`, `assignments_avg`, and `attendance_pct`; the target is `score`. The data was split into **112 training records (75%)** and **38 test records (25%)** using `test_size=0.25` and `random_state=42`. The test set was held out from fitting and used to evaluate performance.

## 3. Performance
On the unseen test set, the model achieved **MAE = 3.329 score points** and **R² = 0.887**. In plain language, its predictions are typically about 3.3 points away from the actual score, and it explains about 88.7% of the variation in scores in this test sample. These are sample-based results and may differ on new cohorts.

## 4. Risks and appropriate use
Predictions can be wrong and may reflect limitations or patterns in this small historical dataset. Students could be harmed if an estimate is treated as a final judgement, used to deny opportunities, or used as the sole basis for grading or disciplinary decisions. Differences in teaching, assessment difficulty, circumstances, and data quality may not be represented. Use predictions only as a preliminary signal to offer supportive review, verify the underlying information, and consider individual circumstances. Do **not** use the model as a replacement for actual assessment, a definitive measure of ability, or an automated decision-maker.
