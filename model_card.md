# Model Card: Student Performance Prediction System

**Student:** Didier Ndahimana  
**Student ID:** 29254  
**Course:** AUCA - Introduction to Big Data Analytics  
**Week:** 10  
**Date:** November 2026

---

## Model Purpose

This machine learning system predicts student academic performance (final scores) and pass/fail outcomes based on attendance, quiz scores, and assignment performance. The model is designed to:

- **Early identification** of at-risk students who may need academic support
- **Performance prediction** to help educators allocate resources effectively
- **Intervention planning** by identifying which factors most strongly influence student success
- **Academic analytics** for program-level and institutional decision-making

The model serves as a decision-support tool for academic advisors and instructors, not as an automated decision-making system.

---

## Data & Features

### Dataset
- **Source:** AUCA student performance data (Week 10 dataset)
- **Size:** 150 students total
- **Split:** 112 training samples (75%) / 38 test samples (25%)
- **Random State:** 42 (for reproducibility)

### Input Features

| Feature | Description | Type | Range |
|---------|-------------|------|-------|
| `attendance_pct` | Percentage of classes attended | Numeric | 0-100% |
| `quiz_avg` | Average quiz score | Numeric | 0-100 |
| `assignments_avg` | Average assignment score | Numeric | 0-100 |

### Target Variables

1. **Regression Target:** `score` (final course score, 0-100)
2. **Classification Target:** `pass` (binary: 0 = fail, 1 = pass, threshold = 50)

### Additional Context Variables
- `student_id`: Unique identifier
- `name`: Student name
- `gender`: Student gender (F/M)
- `program`: Academic program (Information Systems, Software Engineering, Networking, Accounting)
- `district`: Home district

---

## Model Architecture

### Model 1: Linear Regression (Score Prediction)
- **Type:** Multiple Linear Regression
- **Library:** scikit-learn (`sklearn.linear_model.LinearRegression`)
- **Features:** 3 numeric features (attendance, quiz average, assignments average)
- **Output:** Continuous score prediction (0-100)

### Model 2: Logistic Regression (Pass/Fail Classification)
- **Type:** Binary Logistic Regression
- **Library:** scikit-learn (`sklearn.linear_model.LogisticRegression`)
- **Features:** Same 3 numeric features
- **Output:** Binary classification (Pass=1, Fail=0)
- **Threshold:** 50 points

### Feature Engineering Experiments
Three model variants were tested:
1. **Baseline:** Attendance only (R² ≈ 0.62)
2. **Standard:** All three original features (R² ≈ 0.89)
3. **Enhanced:** Original features + engineered features (avg_performance, attendance_performance) (R² ≈ 0.88)

---

## Performance Metrics

### Linear Regression Model (Test Set)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **MAE** | ~3.3 | On average, predictions are within 3.3 points of actual scores |
| **R²** | ~0.89 | Model explains 89% of variance in student scores |

**Interpretation in Plain Language:**  
The model is highly accurate. When predicting a student's final score, it's typically off by only about 3 points out of 100. This level of accuracy is suitable for early warning systems and academic planning.

### Logistic Regression Model (Test Set)

| Metric | Value |
|--------|-------|
| **Accuracy** | ~90-95% |
| **Precision (Pass)** | High |
| **Recall (Pass)** | High |

**Confusion Matrix Analysis:**
- **True Positives:** Students correctly identified as passing
- **True Negatives:** Students correctly identified as at-risk/failing
- **False Positives:** At-risk students incorrectly predicted to pass (critical error)
- **False Negatives:** Passing students incorrectly flagged as at-risk (less critical)

**The Accuracy Trap:**  
While accuracy appears high, it can be misleading if most students pass (class imbalance). The confusion matrix reveals whether the model truly identifies struggling students or simply predicts "pass" for everyone. We specifically monitor **false positives** (missing at-risk students) as these represent missed intervention opportunities.

---

## Model Limitations & Risks

### Known Limitations

1. **Limited Feature Set**
   - Model only considers three quantitative metrics
   - Does not account for: learning disabilities, personal circumstances, mental health, socioeconomic factors, prior education quality, language barriers, or external commitments

2. **Sample Size**
   - Trained on 150 students (112 training samples)
   - May not generalize well to different institutions, countries, or educational systems
   - Performance may vary across different cohorts or academic years

3. **Temporal Limitations**
   - Static snapshot; doesn't capture learning trends over time
   - Cannot predict improvement trajectories or learning velocity

4. **Missing Context**
   - No data on teaching quality, course difficulty, or examination fairness
   - Doesn't account for grade inflation/deflation across programs

### Potential Risks & Mitigation

| Risk | Impact | Mitigation Strategy |
|------|--------|---------------------|
| **Bias & Discrimination** | Model may perpetuate existing biases in grading or attendance tracking | Regular fairness audits across demographic groups; human review of all predictions |
| **Self-Fulfilling Prophecy** | Labeling students as "at-risk" may demotivate them | Present predictions as opportunities for support, not deterministic outcomes |
| **Privacy Concerns** | Student data is sensitive | Strict access controls; anonymization where possible; compliance with data protection laws |
| **Over-Reliance** | Educators may defer judgment to the model | Clearly position model as decision-support tool, not replacement for human judgment |
| **False Sense of Security** | High accuracy may create complacency | Emphasize that model cannot capture all factors; encourage human verification |

### Fairness Considerations

- **Gender:** Model should be evaluated for performance parity across male/female students
- **Program:** Different programs may have different grading standards or difficulty levels
- **District:** Geographic origin should not influence predictions after controlling for performance metrics

**Recommended Practice:** Conduct regular bias audits to ensure predictions are fair across all demographic subgroups.

---

## Usage Guidelines

### Appropriate Uses ✓
- Early identification of students who may benefit from tutoring or support services
- Resource allocation for academic support programs
- Program-level analytics to identify curriculum improvements
- Research into factors affecting student success

### Inappropriate Uses ✗
- **Automated grade assignment** without human review
- **Admission decisions** (model trained on enrolled students only)
- **Disciplinary actions** based solely on predictions
- **Public ranking** or shaming of students
- **Substitute for individualized assessment** by instructors

### Human-in-the-Loop Requirements
- All predictions should be reviewed by qualified academic staff
- Students flagged as at-risk should receive personalized assessment
- Model outputs should inform, not replace, professional judgment
- Students should have right to appeal and provide context

---

## Technical Details

### Training Configuration
- **Training Split:** 75% train / 25% test
- **Random Seed:** 42 (for reproducibility)
- **Validation:** Holdout test set evaluation
- **No hyperparameter tuning** was performed (baseline scikit-learn defaults)

### Software Dependencies
```
Python 3.11+
pandas
numpy
scikit-learn
matplotlib
seaborn
plotly
```

### Model Coefficients (Linear Regression)
- **Attendance:** Positive coefficient (~0.2-0.3) - moderate impact
- **Quiz Average:** Strong positive coefficient (~0.4-0.5) - strongest predictor
- **Assignments Average:** Strong positive coefficient (~0.3-0.4) - second strongest predictor
- **Intercept:** Baseline score when all features are zero

---

## Maintenance & Monitoring

### Recommended Monitoring Schedule
- **Quarterly:** Review prediction accuracy on new cohorts
- **Annually:** Conduct fairness audit across demographic groups
- **Continuous:** Track false positive rate (missed at-risk students)

### Model Retraining Triggers
- Accuracy drops below 85% R²
- Significant curriculum changes
- New grading policies implemented
- Fairness metrics show bias concerns

### Contact for Issues
**Model Owner:** Didier Ndahimana  
**Institution:** Adventist University of Central Africa (AUCA)  
**Course:** Introduction to Big Data Analytics  

---

## References & Acknowledgments

- **Dataset:** AUCA Week 10 Students Dataset (150 records)
- **Framework:** scikit-learn Machine Learning Library
- **Course:** AUCA Big Data Analytics - Week 10 Lab
- **Instructor:** Prince Ishimwe

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2026 | Initial model card for Week 10 submission |

---

## Conclusion

This model demonstrates strong predictive performance (R² = 0.89, MAE = 3.3) for student score prediction. However, it should be used as a **decision-support tool**, not an automated decision system. Human judgment, context, and individual student circumstances must always be considered alongside model predictions.

The model is best suited for early identification of students who may benefit from academic support, allowing educators to proactively offer resources and interventions. Continuous monitoring for bias and fairness is essential to ensure equitable outcomes for all students.

---

*This model card follows responsible AI documentation practices and transparent reporting standards.*
