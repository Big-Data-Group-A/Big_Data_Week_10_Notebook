# Model Card — Student Score Regression

## Purpose
Estimate a student's numeric score from quiz average, assignment average, and attendance. This is a learning exercise and a prompt for supportive academic follow-up, not a grade or consequential decision.

## Data and features
The supplied class data contains 150 records. Inputs: `quiz_avg`, `assignments_avg`, `attendance_pct`. Student names, IDs, gender, program, and district are excluded from the regression model.

## Performance on unseen data
Using a fixed 25% holdout (38 students), the linear regression achieved MAE **3.33 points** and R² **0.89**. Typical absolute error is roughly 3.3 score points; the model explains about 89% of score variation in this test sample.

## Risks and limitations
A wrong estimate could stigmatize a student, misdirect support, or overlook circumstances that these features do not capture. The dataset is small and cohort-specific, so results may not transfer to future classes. Review estimates with the student and instructor, use them only to guide support, and never use them alone to set grades or deny opportunities.
