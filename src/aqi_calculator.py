try:
 pm25=int(input("Enter PM2.5 concentration (µg/m³):"))
 pm10=int(input("Enter PM10 concentration (µg/m³):"))
 NO2=int(input("Enter NO2 concentration (µg/m³):"))
 so2=int(input("Enter SO2 concentration (µg/m³):"))
 co=int(input("Enter CO concentration (µg/m³):"))
 o3=int(input("Enter O3 concentration (µg/m³):"))
except ValueError:
   print("Please Enter valid numeric values")
   exit()
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
def health_advisory():
 if overall_aqi<=50:
   category="good"
   advice=  "Air quality is satisfactory. Enjoy outdoor activities."
 elif overall_aqi<=100:
   category="Satisfactory"
   advice= "Minor breathing discomfort for sensitive people."
 elif overall_aqi<=200:
   category="Moderate"
   advice= "People with lung disease should limit prolonged outdoor exertion."
 elif overall_aqi<=300:
   category="Poor"
   advice= "Breathing discomfort for most people on prolonged exposure."
 elif overall_aqi<=400:
   category="Very Poor"
   advice= "Respiratory illness risk. Avoid outdoor activities."
 else:
   category="Severe"
   advice="Severe health impact. Everyone should avoid outdoor exposure."
 return category,advice
category,advice=health_advisory()
print("\n -----your AQI Report-----")
print("your PM2.5 Level is:",pm25,"µg/m³")
print("your PM10 Level is:",pm10,"µg/m³")
print("your NO2 Level is:",NO2,"µg/m³")
print("your SO2 Level is:",so2,"µg/m³")
print("your CO Level is:",co,"µg/m³")
print("your O3 Level is:",o3,"µg/m³")
print("AQI Value is",round(overall_aqi))
print("Air Quality Category:",category)
print("Dominant Pollutant:", dominant_pollutant)
print("Health Advisory:",advice)
