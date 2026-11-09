## Part 6: The model card

1. Purpose

This model predicts a student’s final score (0 to 100) at AUCA from their quiz average, assignment average, and attendance. It is meant to help lecturers spot students who may be heading for a low score early enough to offer support.

2. Data & features

Trained on 112 students (75% of a 150-student dataset), tested on 38 held-out students. Inputs: quiz_avg, assignments_avg, attendance_pct. The target is score. Student names, program, and district were not used as inputs in the final model.

3. Performance (on unseen data)

On the 38 test students, the model’s predictions are off by about 3.3 points on average (MAE). R² is 0.89, meaning the model explains about 89% of why students’ scores differ. In plain terms: a student predicted at 60 most likely scored between 53 and 63.


4. Risks (who could be harmed, and how to use it)

Who could be harmed: a student wrongly predicted to score low could be labelled “weak”, lose opportunities, or be treated with lower expectations. A student wrongly predicted to do well might not get help they needed. The model is trained on one group of 150 students, so it may be less accurate for students unlike that group.

Use it for: an early-warning signal that prompts a conversation or an offer of support, always checked by a human who knows the student.

Do NOT use it for: assigning grades, deciding admissions, scholarships, or discipline, or making decisions about a student without a lecturer’s judgment. The model also shouldn’t be used to judge programs or districts.
