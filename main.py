import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_excel("week10_students.xlsx")

x = df[["quiz_avg", "assignment_avg", "attendance_pct"]]
y = df["score"]

