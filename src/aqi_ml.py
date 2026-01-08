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

pm25 = float(input("Enter PM2.5: "))
pm10 = float(input("Enter PM10: "))
NO2 = float(input("Enter NO2: "))
so2 = float(input("Enter SO2: "))
co = float(input("Enter CO: "))
o3 = float(input("Enter O3: "))
temp = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
def calculate_aqi(cp,c_low,c_high,i_low,i_high):
    return((i_high-i_low)/(c_high-c_low)*(cp-c_low)+i_low)
def overall_aqi_calculator(pm25,pm10,NO2,so2,co,o3):    
 if pm25<=30:
    aqi_25=calculate_aqi(pm25,0,30,0,50)
 elif pm25<=60:
    aqi_25=calculate_aqi(pm25,31,60,51,100)
 elif pm25<=90:
    aqi_25=calculate_aqi(pm25,61,90,101,200)
 elif pm25<=120:
    aqi_25=calculate_aqi(pm25,91,120,201,300)
 elif pm25<=250:
    aqi_25=calculate_aqi(pm25,121,250,301,400)
 else:
    aqi_25=calculate_aqi(pm25,251,500,401,500)
 if pm10<=30:
    aqi_10=calculate_aqi(pm10,0,50,0,50)
 elif pm10<=60:
    aqi_10=calculate_aqi(pm10,51,100,51,100)
 elif pm10<=90:
    aqi_10=calculate_aqi(pm10,101,250,101,200)
 elif pm10<=120:
    aqi_10=calculate_aqi(pm10,251,350,201,300)
 elif pm10<=250:
    aqi_10=calculate_aqi(pm10,351,430,301,400)
 else:
    aqi_10=calculate_aqi(pm10,431,500,401,500)
 if NO2<=40:
    aqi_NO2=calculate_aqi(NO2,0,40,0,50)
 elif NO2 <= 80:
    aqi_NO2=calculate_aqi(NO2, 41, 80, 51, 100)
 elif NO2 <= 180:
    aqi_NO2=calculate_aqi(NO2, 81, 180, 101, 200)
 elif NO2 <= 280:
    aqi_NO2=calculate_aqi(NO2, 181, 280, 201, 300)
 elif NO2 <= 400:
    aqi_NO2=calculate_aqi(NO2, 281, 400, 301, 400)
 else:
    aqi_NO2=calculate_aqi(NO2, 401, 1000, 401, 500)
 if so2 <= 40:
    aqi_so2 = calculate_aqi(so2, 0, 40, 0, 50)
 elif so2 <= 80:
    aqi_so2 = calculate_aqi(so2, 41, 80, 51, 100)
 elif so2 <= 380:
    aqi_so2 = calculate_aqi(so2, 81, 380, 101, 200)
 elif so2 <= 800:
    aqi_so2 = calculate_aqi(so2, 381, 800, 201, 300)
 elif so2 <= 1600:
    aqi_so2 = calculate_aqi(so2, 801, 1600, 301, 400)
 else:
    aqi_so2 = calculate_aqi(so2, 1601, 2000, 401, 500)
 if co <= 1:
    aqi_co = calculate_aqi(co, 0, 1, 0, 50)
 elif co <= 2:
   aqi_co = calculate_aqi(co, 1.1, 2, 51, 100)
 elif co <= 10:
   aqi_co = calculate_aqi(co, 2.1, 10, 101, 200)
 elif co <= 17:
   aqi_co = calculate_aqi(co, 10.1, 17, 201, 300)
 elif co <= 34:
   aqi_co = calculate_aqi(co, 17.1, 34, 301, 400)
 else:
   aqi_co = calculate_aqi(co, 34.1, 50, 401, 500)
 if o3 <= 50:
   aqi_o3 = calculate_aqi(o3, 0, 50, 0, 50)
 elif o3 <= 100:
   aqi_o3 = calculate_aqi(o3, 51, 100, 51, 100)
 elif o3 <= 168:
   aqi_o3 = calculate_aqi(o3, 101, 168, 101, 200)
 elif o3 <= 208:
   aqi_o3 = calculate_aqi(o3, 169, 208, 201, 300)
 elif o3 <= 748:
   aqi_o3 = calculate_aqi(o3, 209, 748, 301, 400)
 else:
   aqi_o3 = calculate_aqi(o3, 749, 1000, 401, 500)
 aqi_values = {
    "pm25":aqi_25,
    "pm10":aqi_10,
    "NO2":aqi_NO2,
    "SO2":aqi_so2,
    "CO":aqi_co,
    "O3":aqi_o3
 }
 dominant_pollutant = max(aqi_values)
 overall_aqi = aqi_values[dominant_pollutant]
 return overall_aqi, dominant_pollutant
overall_aqi, dominant_pollutant = overall_aqi_calculator(pm25, pm10, NO2,so2,co,o3)
new_data = pd.DataFrame(
    [[pm25, pm10, temp, humidity]],
    columns=['PM2.5', 'PM10', 'Temperature', 'Humidity']
)

ml_aqi = model.predict(new_data)[0]
rule_aqi = overall_aqi


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
