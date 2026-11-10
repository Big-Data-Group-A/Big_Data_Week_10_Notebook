    Model Card — Student Score Predictor

    1. Purpose
    Predicts a student's final exam score (0–100) before the exam, using quiz average, assignment average, and attendance. Intended for academic advisors to identify students who may need extra support — not for students to see their score in advance.

    2. Data & features
    Trained on 150 AUCA students (Week 10 dataset), split 112 train / 38 test. Three features: quiz_avg, assignments_avg, attendance_pct. Target: score. Tested with test_size=0.25, random_state=42.

    3. Performance (on unseen test data)

        MAE ≈ 3.3 points — predictions are typically within ~3 exam points of reality.

        R² ≈ 0.89 — the model explains 89% of the variation in scores. The remaining 11% comes from factors we didn't measure (health, home life, motivation, teaching quality).

    4. Risks

        Stigma & self-fulfilling prophecy: labelling a student "likely to fail" can demoralise them and change their behaviour.

        Bias: if past scores reflect unfairness by gender, district, or wealth, the model automates that unfairness at scale (correlation ≠ causation; bias replicates — slide 11).

        Over-trust: an R² of 0.89 is high, but 11% of variation is unexplained.

        How it SHOULD be used: as a conversation starter for advisors to reach out with support — one signal among many.

        How it should NOT be used: to automatically fail a student, deny a scholarship, or show the predicted score to the student as a verdict.

