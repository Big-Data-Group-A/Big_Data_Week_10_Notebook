# Model Card — Final Score Predictor

**Course:** Introduction to Big Data Analytics, Week 10 Lab
**Author:** Hirwa Ngenzi Honore
**Model type:** Linear regression (scikit-learn `LinearRegression`)

## 1. Purpose

This model predicts a student's final score (0–100) from three numbers: their quiz average, their assignments average and their attendance percentage.

It is meant for lecturers and programme coordinators at AUCA. They can use it as an early signal to notice students who may need extra support, before the final results come out.

## 2. Data and Features

- **Data:** 150 students across four programmes (Accounting, Information Systems, Networking, Software Engineering) and eight districts. The data is clean, with no missing values.
- **Split:** 112 students (75%) were used to train the model. 38 students (25%) were kept hidden and used only to test it (`test_size=0.25`, `random_state=42`).
- **Features used:** `quiz_avg`, `assignments_avg`, `attendance_pct`.
- **Target:** `score`.
- **What matters most:** quiz average. One extra quiz point is worth about 0.58 exam points, assignments about 0.36 and attendance about 0.11 (each holding the other two fixed).
- **Not used:** programme, district, gender and student name. Adding programme did not improve the model (R² went from 0.89 to 0.88).

## 3. Performance

Both numbers below were measured on the 38 test students, whom the model had never seen.

| Metric | Value | What it means in plain language |
|---|---|---|
| MAE (mean absolute error) | about 3.3 points | On average, the prediction is off by about 3 marks out of 100. If the model says 60, the real score is usually around 57 to 63. |
| R² | about 0.89 | The model explains about 89% of the differences between students' scores. The other 11% comes from things it cannot see. |

Quiz average alone gives R² of only 0.62, so using all three features helps a lot.

The model was tested on only 38 students, so these numbers are a good guide but not exact. Results may differ for a different group of students.

## 4. Risks and Appropriate Use

**Who could be harmed by a wrong prediction**
- A student who is predicted to do badly but would actually do well could be labelled "weak". This can lower people's expectations of them or cost them opportunities.
- A student who is predicted to do well but is actually struggling could be missed and not get help.

**Limits of the model**
- It sees only three numbers. It knows nothing about illness, family problems, effort, language or other things that affect a student's results.
- It was trained on only 150 students, so it may not work well for other years, programmes or schools.
- It can be less reliable for unusual students, such as those with very high or very low scores.

**How it should be used**
- As an early-warning signal that starts a conversation and leads to support for the student.
- Always with a person reviewing the result before any action is taken.

**How it should NOT be used**
- To decide a student's grades, admission, scholarship or discipline.
- As the only reason to judge or label a student.
- To compare students publicly or rank them.
