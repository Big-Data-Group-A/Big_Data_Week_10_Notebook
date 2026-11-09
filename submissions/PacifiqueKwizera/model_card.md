# Linear Regression Coursework Predictor Model Card

## 1. Purpose
- **What does it predict?** Continuous final examination score (scale 0–100).
- **For whom?** Course instructors, academic advisors, and the AUCA Faculty Dean.
- **Objective:** Provide a formative early-warning indicator midway through the semester so instructors can proactively support students before final examinations occur.

## 2. Data & Features
- **Input Dataset:** `week10_students.csv` containing 150 AUCA undergraduate student records across five academic programs (Software Engineering, Information Systems, Networking, Accounting, etc.).
- **Predictor Features:**
  1. `attendance_pct`: Class attendance percentage (0–100%).
  2. `quiz_avg`: Weighted mean of in-class timed quizzes (0–100%).
  3. `assignments_avg`: Average score on laboratory assignments and homework (0–100%).
- **Target Variable:** `score` (continuous final exam score, 0–100).
- **Validation Strategy:** 75% train ($N=112$) / 25% test ($N=38$) with fixed seed `random_state=42`.

## 3. Performance (Evaluated on Unseen Test Cohort)
- **Mean Absolute Error (MAE):** ≈ 3.3 points (3.33).
  - *Plain Language:* On completely unseen students, the model's predicted final score lands within approximately 3.3 percentage points of their true grade.
- **Coefficient of Determination ($R^2$):** ≈ 0.89 (0.8866).
  - *Plain Language:* 89% of the variance in student outcomes is directly attributable to their combined attendance, quiz mastery, and assignment diligence. Only 11% is due to unobserved factors (exam-day stress, health, unrecorded study hours).

## 4. Risks & Ethical Considerations
- **Who could be harmed by a wrong prediction?**
  - *False Over-Optimism (Under-flagging):* If an at-risk student is erroneously predicted to pass, they may fail to seek necessary tutoring, leading to course failure.
  - *False Pessimism (Over-flagging):* Underestimating a student's potential could induce unnecessary anxiety or create negative instructor bias (Pygmalion effect).
- **How the output SHOULD be used:**
  - As an advisory, diagnostic prompt to trigger voluntary academic tutoring, peer-assisted study groups, and instructor check-ins.
- **How the output MUST NOT be used:**
  - The model must **never** be used for automated summative grading, academic probation determinations, scholarship revocation, or barring students from taking examinations.
