"""String operations via the .str accessor."""
import pandas as pd

df = pd.DataFrame({
    "email": ["Alice@Example.COM", "  bob@test.com  ", "CHARLIE@WORK.ORG"]
})

df["email"]    = df["email"].str.strip().str.lower()
df["domain"]   = df["email"].str.split("@").str[1]
df["is_work"]  = df["email"].str.contains("work")

print(df)
