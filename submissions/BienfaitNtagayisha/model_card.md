# Model Card — Student Score Predictor

## 1. Purpose
Predicts a student's final exam score (0–100) from their quiz average,
assignment average, and attendance percentage. Built for AUCA instructors
and academic advisors as an early-warning tool — NOT for ranking, punishing,
or grading students.

## 2. Data & Features
- Source: `week10_students.csv` (150 AUCA students).
- Features used: `quiz_avg`, `assignments_avg`, `attendance_pct`.
- Target: `score`.
- Train/test split: 75% / 25% with `random_state=42` (112 train / 38 test).

## 3. Performance (on unseen test data)
- MAE ≈ 3.33 points → predictions are typically within about
  3.3 points of the true score.
- R² ≈ 0.89 → the model explains ~88% of the variation in
  student scores.
- Plain language: on average the model gets the score right to within a
  few points, but individual predictions can be off by much more for
  students whose situation is not captured by these three features.

## 4. Risks & Intended Use
- **Who could be harmed**: a student wrongly flagged as at-risk may be
  stigmatized or given unnecessary remediation; a student wrongly marked
  safe could miss support they actually need.
- **Use it FOR**: starting conversations, prioritising who gets tutoring
  or advisor check-ins, spotting patterns in a cohort.
- **Do NOT use it**: as a final grade, as grounds for discipline, to deny
  scholarships or placements, or to label a student as "good" or "bad".
- **Human oversight**: every decision about a real student must be made
  by a human who knows their circumstances, not by this model alone.
