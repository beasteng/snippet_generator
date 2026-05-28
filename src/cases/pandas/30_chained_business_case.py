"""Full chained pipeline — realistic interview scenario."""
import pandas as pd

# --- Raw data ---
df = pd.DataFrame({
    "dept":      ["IT", "IT", "HR", "HR", "HR", "Sales", "Sales"],
    "employee":  ["A",  "B",  "C",  "D",  "E",  "F",     "G"],
    "salary":    [100,  150,  80,   120,  110,   90,      130],
    "join_date": ["2024-01-01", "2024-03-15", "2024-02-01",
                  "2024-04-01", "2024-04-10", "2023-12-01", "2024-06-01"]
})

result = (
    df
    .assign(join_date=lambda x: pd.to_datetime(x["join_date"]))
    .assign(tenure_days=lambda x: (pd.Timestamp("2026-05-27") - x["join_date"]).dt.days)
    .query("salary >= 90")
    .groupby("dept", as_index=False)
    .agg(
        avg_salary   = ("salary", "mean"),
        total_salary = ("salary", "sum"),
        headcount    = ("employee", "count"),
        avg_tenure   = ("tenure_days", "mean")
    )
    .sort_values("avg_salary", ascending=False)
    .reset_index(drop=True)
)

print(result)
# Interview tip: chaining .assign().query().groupby().agg().sort_values()
# shows you know the pandas fluent API — big plus.
