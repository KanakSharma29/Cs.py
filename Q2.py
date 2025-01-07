# Less than 0°C--	Heavy winter clothing: Thick coats, gloves, scarf, thermal wear, boots.
# 0°C to 10°C--	Winter clothing: Coat, sweater, warm pants, and possibly a hat and gloves.
# 11°C to 20°C---Light jacket or sweater: Suitable for mild cold weather.
# 21°C to 30°C--Comfortable casual clothing: T-shirt, jeans, or light dresses.
# 31°C to 40°C---	Light and breathable clothing: Shorts, cotton t-shirts, avoid heavy fabrics.
# Above 40°C--Extremely light clothing: Sleeveless tops, shorts, sun protection (hat, sunscreen).

temp = int(input("Enter the temprature in celsius:"))

if temp < 0:
    print("Recommended Clothing:Heavy winter clothing (e.g., thick coat, gloves, scarf, and thermal wear")
elif 0 <= temp <= 10:
    print("Recommended Clothing:Winter clothing (e.g., coat, sweater, and warm pants)")
elif 11 <= temp <=20:
    print("Recommended Clothing:Light jacket or sweater with full pants")
elif 21 <= temp <= 30:
    print("Recommended Clothing:Comfortable casual clothing (e.g., t-shirt and jeans)")
elif 31 <= temp <=40:
    print("Recommended Clothing:Light and breathable clothing (e.g., shorts and cotton t-shirt)")
else:
    print("Recommended Clothing:Extremely light clothing: Sleeveless tops, shorts, sun protection (hat, sunscreen)")