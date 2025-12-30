pm25=int(input("Enter PM2.5 concentration (µg/m³):"))
pm10=int(input("Enter PM10 concentration (µg/m³):"))
def calculate_aqi(pm25,c_low,c_high,i_low,i_high):
    return((i_high-i_low)/(c_high-c_low)*(pm25-c_low)+i_low)
def overall_aqi_calculator(pm25,pm10):    
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
 if aqi_25>aqi_10:
    dominant_pollutant= "pm25"
    overall_aqi= aqi_25
 else:
    dominant_pollutant= "pm10"
    overall_aqi= aqi_10
 return overall_aqi, dominant_pollutant
overall_aqi, dominant_pollutant= overall_aqi_calculator(pm25,pm10)
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
print("AQI Value is",round(overall_aqi))
print("Air Quality Category:",category)
print("Dominant Pollutant:", dominant_pollutant)
print("Health Advisory:",advice)
