# Week 10 Lab: Machine Learning & Dashboards

**Course:** Introduction to Big Data Analytics, AUCA
**Instructor:** Prince Ishimwe
**student:**  Ishimwe muhire johnson

This project trains two machine learning models on a dataset of 150 students. It then publishes an interactive chart.

- A **regression** model predicts a student's final score.
- A **classification** model flags students who are at risk of failing.

---

## Files

| File | What it is |
|---|---|
| `week10_students.xlsx` | Original data (Excel) |
| `week10_students.csv` | Same data converted to CSV |
| `Week10_ishimwe_muhire_johnson_20252SEN147.ipynb` | The notebook with all the code, answers and model card |
| `class_dashboard.html` | Interactive "Who is at risk" chart (open in a browser) |
| `README.md` | This file |

---

## The dataset

150 students, no missing values.

| Column | Meaning |
|---|---|
| `student_id` | Unique ID, e.g. AUCA001 |
| `name` | Student name |
| `gender` | F or M |
| `program` | Information Systems, Software Engineering, Networking or Accounting |
| `district` | Home district |
| `attendance_pct` | Attendance percentage |
| `quiz_avg` | Average quiz mark |
| `assignments_avg` | Average assignment mark |
| `score` | Final score (**the target we predict**) |

---

## How to run

### Option A: Google Colab (easiest)
1. Go to [colab.research.google.com](https://colab.research.google.com) and upload `Week10_YourName.ipynb`.
2. Upload `week10_students.xlsx` (and the CSV) using the folder icon on the left.
3. Click **Runtime → Run all**.

Everything you need is already installed in Colab.

### Option B: Anaconda / Jupyter on your computer
1. Put the notebook and the data files in the same folder.
2. Install the libraries if needed:
   ```
   pip install pandas scikit-learn plotly openpyxl
   ```
3. Open the notebook in Jupyter and choose **Kernel → Restart & Run All**.

The first code cell reads the Excel file and saves it as `week10_students.csv`. Keep `week10_students.xlsx` next to the notebook so that cell works.

---

## What the notebook does

| Part | Task | Marks |
|---|---|---|
| 1 | Explore the data, check correlations, split into train/test | 5 |
| 2 | Linear regression: train, evaluate, predict a new student | 10 |
| 3 | Logistic regression: pass/fail model and the accuracy trap | 8 |
| 4 | Feature engineering: does more information help? | 5 |
| 5 | Three Plotly charts and the saved dashboard | 7 |
| Bonus | Box plot of scores by program | +3 |
| 6 | Model card (required) | checked for completion |

Every split uses `test_size=0.25, random_state=42`, so your numbers match the checkpoints.

---

## Results

| Check | Result |
|---|---|
| Data shape | 150 rows × 9 columns |
| Train / test sizes | 112 / 38 |
| Strongest feature | `quiz_avg` (correlation 0.80) |
| Regression MAE | about 3.33 points |
| Regression R² | about 0.89 |
| Pass / fail counts | 131 passed, 19 failed |
| Classifier accuracy | 0.895 |
| Lazy baseline ("everyone passes") | 0.895 |
| Confusion matrix | `[[3, 1], [3, 31]]` |
| R² by feature set | 0.62 (quiz only) → 0.89 (three features) → 0.88 (+ program) |

**Key lessons**
- Accuracy alone can mislead when most students pass. The confusion matrix shows our model still catches 3 of the 4 failing students, while the lazy model catches none.
- Adding more features only helps when they carry new information.

---

## Key terms

| Term | Plain meaning |
|---|---|
| **Feature (X)** | The clues used to predict (quiz, assignments, attendance) |
| **Target (y)** | The answer we want to predict (score) |
| **Train / test split** | Practise on 75% of students, then get graded on the 25% the model has never seen |
| **MAE** | Average size of the model's mistakes, in score points |
| **R²** | How much of the differences between students the model explains (0 to 1) |
| **Confusion matrix** | A table of right and wrong predictions for each class |
| **One-hot encoding** | Turning text categories into 0/1 columns with `pd.get_dummies` |

---

## Model card (summary)

- **Purpose:** predicts a student's final score from quiz, assignments and attendance, to help lecturers spot students who need support early.
- **Performance:** typically about 3 marks off; explains about 89% of score differences on unseen students.
- **Risks:** a wrong prediction could wrongly label a student or miss one who needs help. The model is trained on only 150 students.
- **Use for:** an early-warning signal that starts a human conversation.
- **Do NOT use for:** final grades, pass/fail decisions, discipline or scholarships.

The full model card is at the end of the notebook.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: plotly` | Run `pip install plotly` |
| `FileNotFoundError: week10_students.xlsx` | Put the Excel file in the same folder as the notebook |
| Excel reading error | Run `pip install openpyxl` |
| Different numbers from the checkpoints | Check you used `test_size=0.25, random_state=42` in every split |
| `class_dashboard.html` looks empty | Open it in Chrome, Edge or Firefox, not inside a text editor |

---

