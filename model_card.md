# Model Card — Student Score Predictor
**Author:** Manzi Fred | **ID:** 26634

**1. Purpose**
    Predicts a final score (0-100) to spot students needing help early.

**2. Data**
    150 AUCA students, week10_students.xlsx

**3. Features**
    quiz_avg (0.58), assignments_avg (0.36), attendance_pct (0.11)

**4. Split**
    112 train / 38 test, random_state = 42

**5. Performance (test set)**
    - MAE = 3.3 points — off by ~3 marks on average
    - R²  = 0.89     — explains 89% of score differences

**6. Risks**
    Wrong low prediction can demotivate a student;
    wrong high prediction can miss a student who needs help.

**7. Use for**
    Tutoring / early-warning intervention

**8. Not for**
    Making pass/fail decisions or scholarship eligibility alone.
