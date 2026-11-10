## Part 6 · Model Card — Exam Score Predictor

**1. Purpose.** Predicts a student's final score (0–100) from their quiz average, assignment average and attendance. It is meant for AUCA lecturers and advisors to spot students who may need support early in the semester.

**2. Data & features.** 150 AUCA students (clean data). Inputs: `quiz_avg`, `assignments_avg`, `attendance_pct`. Target: `score`. Names, gender, district and program were not used. Model: linear regression trained on 112 students (75%).

**3. Performance (38 unseen students).** MAE ≈ 3.3 points: the prediction is typically within about 3 marks of the real score. R² ≈ 0.89: the three inputs explain about 89% of the differences in scores. Quiz average matters most (about +0.58 points per quiz point). The model is built on one small class and may not hold for other cohorts or courses.

**4. Risks.** A wrong prediction could wrongly label a student as weak (lower expectations, lost opportunities) or falsely reassure a student who then gets no help. Errors of a few points matter near the pass mark of 50. *Use for:* prioritising extra support, tutoring and early conversations. *Do NOT use for:* grading, deciding who passes, admissions, scholarships or discipline, or as the only basis for judging a person. A human should always review the output, and the model should be re-checked each new cohort.