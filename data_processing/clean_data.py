import pandas as pd

df = pd.read_excel('../data/processed/2025/00_2025.xlsx')

print(df.info())
print()
print(df.to_string())
