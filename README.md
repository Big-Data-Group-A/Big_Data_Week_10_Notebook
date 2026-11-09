# Week 10 Lab — Machine Learning & Dashboards

**AUCA · Introduction to Big Data Analytics**
Instructor: Prince Ishimwe · Prince.ishimwe@auca.ac.rw
Total: 35 marks (+3 bonus) · Due: end of Week 10

Train · Evaluate · Predict · Publish

---

## 📁 What's in this repo

| File | Purpose |
|------|---------|
| `Lab 5.pdf` | The lab instructions (all exercises, marking scheme, checklist) |
| `week10_students.xlsx` | The dataset: 150 clean students |
| `README.md` | This guide |

**Dataset columns:** `student_id`, `name`, `gender`, `program`, `district`, `attendance_pct`, `quiz_avg`, `assignments_avg`, `score` (the target).

> The lab PDF mentions `week10_students.csv`. The file provided is an Excel file, so either:
> - load it directly: `df = pd.read_excel("week10_students.xlsx")`, or
> - open it in Excel/Sheets, **Save As → CSV**, name it `week10_students.csv`, and use `pd.read_csv(...)`.
>
> Keep the data file next to your notebook.

---

## 🧪 What you need to do (summary)

Read `Lab 5.pdf` for the full details. In short:

| Part | Topic | Marks |
|------|-------|-------|
| 1 | Explore & split (`test_size=0.25, random_state=42` → 112 train / 38 test) | 5 |
| 2 | Linear regression: coefficients, MAE/R² on the **test** set, predict new students | 10 |
| 3 | Logistic regression: pass/fail, the accuracy trap and confusion matrix | 8 |
| 4 | Feature engineering: compare R² of 3 models | 5 |
| 5 | Plotly dashboard: 3 charts + save `class_dashboard.html` | 7 |
| Bonus | Box plot by program + two sentences | +3 |
| 6 | Model card (required, checked for completion) | — |

Use `test_size=0.25, random_state=42` in **every** split so your numbers match the checkpoints.
Colab has everything pre-installed. On Anaconda, run `pip install plotly` if the import fails.

---

## 📦 What you must submit

Put these four things in your submission folder:

1. **Completed notebook**, named `Week10_YourName.ipynb`
2. **`class_dashboard.html`** and a **screenshot of it open in your browser** (e.g. `dashboard_screenshot.png`)
3. **Model card** (purpose, data & features, performance in plain language, risks), as `model_card.md` or inside the notebook
4. **Screenshots** of your key outputs (e.g. checkpoints, confusion matrix)

Your folder should look like this:

```
submissions/
└── YourName/
    ├── Week10_YourName.ipynb
    ├── class_dashboard.html
    ├── dashboard_screenshot.png
    ├── model_card.md
    └── screenshots/
        ├── 01_split_sizes.png
        └── ...
```

---

## 🚀 How to submit (branch only, NO Pull Request)

You submit by **pushing your own branch** to this repository.
**Do NOT open a Pull Request.** Do NOT push to `main`. Your branch *is* your submission.

### Before you start

- You need a GitHub account and [Git installed](https://git-scm.com/downloads).
- You must have **write access** to this repo. If `git push` is rejected with a permission error (403), ask the instructor to add you as a collaborator.

### Step 1: Clone the repository

```bash
git clone https://github.com/Big-Data-Group-A/Big_Data_Week_10_Notebook.git
cd Big_Data_Week_10_Notebook
```

### Step 2: Create your own branch

Name it `firstname-lastname` (lowercase, hyphens, no spaces). Example for Aline Uwase:

```bash
git checkout -b aline-uwase
```

### Step 3: Do the lab and add your files

Create your folder and put your deliverables inside it:

```bash
mkdir -p submissions/AlineUwase
# copy your notebook, class_dashboard.html, screenshots and model card into it
```

Only add files inside **your own** `submissions/YourName/` folder. Never edit other students' files or the lab files.

### Step 4: Commit your work

```bash
git add submissions/AlineUwase
git status                      # check that only your files are listed
git commit -m "Week 10 submission - Aline Uwase"
```

### Step 5: Push your branch

```bash
git push -u origin aline-uwase
```

That's it, you're done. ✅
Go to the repo on GitHub → the **branch dropdown** and confirm your branch and files appear.

> 🛑 GitHub will show a yellow banner saying **"Compare & pull request"**. **Ignore it. Do not click it.**

### Updating your submission (before the deadline)

Made a fix? Commit and push again on the same branch:

```bash
git add submissions/AlineUwase
git commit -m "Update Week 10 submission"
git push
```

---

## ✅ Submission checklist

- [ ] Notebook renamed `Week10_YourName`
- [ ] Split sizes show 112 train / 38 test
- [ ] Regression evaluated on the **TEST** set (MAE ≈ 3.3, R² ≈ 0.89)
- [ ] Confusion-matrix argument written (comment, Exercise 3.2d)
- [ ] Feature-engineering comparison done (≈ 0.62 → 0.89 → 0.88)
- [ ] `class_dashboard.html` saved **+ screenshot** of it open in the browser
- [ ] Model card written
- [ ] Notebook is saved **with outputs visible** (run all cells before saving)
- [ ] Branch pushed to GitHub; **no PR opened**
- [ ] Submitted before the end of Week 10

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---------|-----|
| `Permission denied` / `403` on push | You're not a collaborator yet. Ask the instructor for access. |
| `git push` says "no upstream branch" | Use `git push -u origin your-branch-name` the first time. |
| `Author identity unknown` on commit | Run `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`. |
| Pushed to `main` by mistake | Tell the instructor right away. Don't try to fix it with force-push. |
| Large notebook/HTML refuses to push | Files must be under 100 MB. Compress screenshots if needed. |
| Notebook built in Colab | **File → Download → Download .ipynb**, then add it to your folder. |

Good luck! 🎓
