# Model Card: Student Score Predictor

**Course:** Introduction to Big Data Analytics, AUCA (Week 10 Lab) **Name:** ishimwe muhire johnson  **Model type:** Linear regression (scikit-learn `LinearRegression`)

## 1. Purpose

This model predicts a student's final score (0 to 100) from three things: their quiz average, their assignments average and their attendance. It is meant for AUCA lecturers and academic advisors, to spot students who may need help early in the semester, while there is still time to support them.

## 2. Data and features

The model was trained on 150 clean student records from `week10_students.csv`. The data was split randomly with `test_size=0.25` and `random_state=42`: 112 students were used to train the model and 38 were kept hidden to test it.

**Features (inputs):**

- `quiz_avg`: average quiz mark
- `assignments_avg`: average assignment mark
- `attendance_pct`: percentage of classes attended

**Target (output):** `score`, the student's final score.

**Not used:** name, student ID, gender, district and program. We tested adding program and it did not help (R² went from 0.89 to 0.88), so we left it out. Gender and district were left out on purpose, because a prediction should not depend on who a student is or where they come from.

**What the model learned:**

| Feature | Weight |
| --- | --- |
| quiz\_avg | 0.58 |
| assignments\_avg | 0.37 |
| attendance\_pct | 0.11 |
| Intercept | -4.43 |

In plain words, one extra quiz point adds about 0.58 points to the predicted score, and quiz marks matter most.

## 3. Performance

These numbers come from the 38 students the model had never seen.

- **MAE = 3.3 points.** On average, the prediction is wrong by about 3 marks out of 100. If a student really scored 60, the model would typically say something between 57 and 63.
- **R² = 0.89.** The model explains about 89% of the differences between students' scores. The remaining 11% comes from things the model cannot see, such as illness, family problems or a bad exam day.

A dean can read this as: the model is a good guide, but it is an estimate and not a guarantee.

## 4. Risks and responsible use

**Who could be harmed by a wrong prediction?**

- A capable student wrongly predicted to score low could be labelled "at risk", face lowered expectations or be treated unfairly.
- A struggling student wrongly predicted to score well could be missed and get no help.

**Limits of the model:**

- It was trained on only 150 students, and it may not work for other courses, years or universities.
- It only sees three numbers. It knows nothing about a student's circumstances.
- It was tested on one split of the data, so the 3.3 and 0.89 could change a little with different students.

**Use it for:**

- An early-warning signal that starts a conversation between a lecturer and a student.
- Deciding who to offer extra tutoring or check-ins to.

**Do NOT use it for:**

- Final grades or pass/fail decisions.
- Discipline, scholarships or ranking students.
- Any decision made without a human reviewing the student's full situation.
