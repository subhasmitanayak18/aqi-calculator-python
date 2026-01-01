import pandas as pd
data = pd.read_csv(r"C:\OLIVIA\PYTHONFOLDER\project\data\air_quality_data.csv")
print(data.head())
print("\nDataset info:",data.info())
print("\nStatistical Summary:",data.describe())