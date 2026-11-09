# Model Card --- Week 10 Machine Learning Lab

## 1. Model Purpose

This project uses student academic data to predict a student's numerical
score with Linear Regression and classify whether a student passes or
fails with Logistic Regression. A score of 50 or above is treated as a
pass.

## 2. Dataset

The project uses `week10_students.csv`, containing 150 student records
and 9 columns.

## 3. Features Used

The main numerical input features are: - `quiz_avg` --- quiz average. -
`assignments_avg` --- assignments average. - `attendance_pct` ---
attendance percentage.

The `program` feature was also tested using one-hot encoding in the
feature-comparison experiment.

## 4. Model Performance

### Linear Regression

-   Mean Absolute Error (MAE): 3.3292 (approximately 3.33 marks).
-   R² score: 0.8866.

The model's predictions were, on average, about 3.33 marks away from the
actual scores in the test set. The R² score indicates that the model
explained approximately 88.66% of the variation in test scores.

### Logistic Regression

-   Accuracy: 89.47%.
-   All-pass baseline accuracy: 89.47%.
-   Confusion matrix: `[[3, 1], [3, 31]]`.

The Logistic Regression model achieved the same accuracy as the all-pass
baseline. It correctly identified 3 failing students and 31 passing
students, but it also made 1 false-pass prediction and 3 false-fail
predictions. Therefore, its accuracy does not show an improvement over
the baseline, and it has limited ability to identify failing students.

## 5. Feature Comparison

  Feature set                         R² score
  --------------------------------- ----------
  Quiz average only                     0.6242
  All three numerical features          0.8866
  Numerical features plus program       0.8804

The model using all three numerical features produced the highest R²
score among the tested feature sets.

## 6. Intended Use

These models are intended for educational analysis and as a learning
exercise in predicting scores and classifying pass/fail outcomes. Their
outputs may help explore patterns in the supplied dataset.

## 7. Risks and Limitations

-   The dataset contains only 150 students and may not represent a wider
    student population.
-   Predictions are estimates, not guaranteed actual results.
-   The pass/fail model achieved the same accuracy as the all-pass
    baseline.
-   The confusion matrix shows that the pass/fail model has limited
    ability to identify failing students.
-   The dataset may omit other factors that influence academic
    performance.
-   The models should not be used as the sole basis for consequential
    academic decisions.
