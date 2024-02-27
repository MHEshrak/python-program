temperature = float(input("enter the temperature ( celsius or fahrenheit ) : "))
input_unit = input("choose a unit to convert (C or F ): ")
conversion = input_unit.upper()

if conversion == "C":
    result = 5 / 9 * (temperature - 32)
    unit = "celsius"
    print(f"the temperature is {round(result, 1)}°C {unit}")
elif conversion == "F":
    result = (temperature * (9 / 5)) + 32
    unit = "fahrenheit"
    print(f"the temperature is {round(result, 1)}°F {unit}")
else:
    print("you didn't enter correct value.")
