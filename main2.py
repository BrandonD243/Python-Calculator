#WEATHER FORECAST
temp = float(input("Enter the temperature: "))

while True:
    sunny = input("Is it sunny outside? (Y/N)")
    if sunny == "Y":
        is_sunny = True
        break
    elif sunny == "N":
        is_sunny = False
        break
    else:
        print(f"{sunny} is an invalid entry.")


if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")