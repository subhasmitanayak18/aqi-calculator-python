import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


df = pd.read_csv(r"C:\OLIVIA\PYTHONFOLDER\project\data\air_quality_data.csv")
df = df.dropna()
print(df.head())
print(df.info())
X = df[['PM2.5', 'PM10', 'Temperature', 'Humidity']]
y = df['AQI']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)
# ---------- Predict AQI for new input ----------
pm25 = float(input("Enter PM2.5: "))
pm10 = float(input("Enter PM10: "))
temp = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))

new_data = [[pm25, pm10, temp, humidity]]
predicted_aqi = model.predict(new_data)

print("\nPredicted AQI:", round(predicted_aqi[0]))
