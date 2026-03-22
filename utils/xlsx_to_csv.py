import pandas as pd
import os

excel_file = 'data/online_retail.xlsx'
csv_file = 'data/online_retail.csv'

df = pd.read_excel(excel_file)
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f"Successfully converted '{excel_file}' to '{csv_file}'")