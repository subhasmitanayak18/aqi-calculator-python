import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


df = pd.read_csv(r"C:\OLIVIA\PYTHONFOLDER\project\data\air_quality_data.csv")
df.dropna(inplace=True)

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


def rule_based_aqi(pm25):
    if pm25 <= 30:
        return (50 / 30) * pm25
    elif pm25 <= 60:
        return ((100 - 51) / (60 - 31)) * (pm25 - 31) + 51
    elif pm25 <= 90:
        return ((200 - 101) / (90 - 61)) * (pm25 - 61) + 101
    elif pm25 <= 120:
        return ((300 - 201) / (120 - 91)) * (pm25 - 91) + 201
    elif pm25 <= 250:
        return ((400 - 301) / (250 - 121)) * (pm25 - 121) + 301
    else:
        return ((500 - 401) / (500 - 251)) * (pm25 - 251) + 401


pm25 = float(input("Enter PM2.5: "))
pm10 = float(input("Enter PM10: "))
temp = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))

new_data = pd.DataFrame(
    [[pm25, pm10, temp, humidity]],
    columns=['PM2.5', 'PM10', 'Temperature', 'Humidity']
)

ml_aqi = model.predict(new_data)[0]
rule_aqi = rule_based_aqi(pm25)


print("\n" + "═" * 42)
print("        🌍 AQI PREDICTION REPORT")
print("═" * 42)

print("\n📥 Input Parameters")
print("-" * 42)
print(f"PM2.5        : {pm25}")
print(f"PM10         : {pm10}")
print(f"Temperature  : {temp} °C")
print(f"Humidity     : {humidity} %")

print("\n📊 AQI Results")
print("-" * 42)
print(f"Rule-based AQI   : {round(rule_aqi)}")
print(f"ML Predicted AQI : {round(ml_aqi)}")

print("\n🔍 Model Performance")
print("-" * 42)
print(f"Mean Absolute Error : {mae:.2f}")
print(f"R² Score            : {r2:.3f}")

print("\n⚠️ Insight")
print("ML smooths extreme values based on learned patterns")
print("instead of fixed threshold jumps.")

print("\n" + "═" * 42)
