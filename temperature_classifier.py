def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif temp <= 25:
        return "Normal"
    elif temp <= 35:
        return "Warm"
    else:
        return "Hot"


temperatures = [10, 20, 30, 40]

for temp in temperatures:
    print(temp, "°C =", classify_temperature(temp))
