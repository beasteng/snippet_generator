"""Map values via dictionary or function."""
import pandas as pd

df = pd.DataFrame({
    "grade": ["A", "B", "C", "A", "B"]
})

grade_to_gpa = {"A": 4.0, "B": 3.0, "C": 2.0}
df["gpa"] = df["grade"].map(grade_to_gpa)

# replace() works similarly for multiple columns
df["pass"] = df["grade"].map(lambda g: "Yes" if g in ("A", "B") else "No")

print(df)
