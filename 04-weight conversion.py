weight = float(input("enter your weight ( kilogram or pound) : "))
input_unit = input("choose a unit to convert (K or P): ")
conversion = input_unit.upper()

if conversion == "K":
    result = weight * 2.205
    unit = "Kg"
    print(f"your weight is {round(result, 3)} {unit}")
elif conversion == "P":
    result = weight / 2.205
    unit = "Lb"
    print(f"your weight is {round(result, 3)} {unit}")
else:
    print("you didn't enter correct value.")
