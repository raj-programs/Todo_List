# Simple Temperature Converter

temp = float(input("Enter temperature: "))
unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip().upper()

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C = {converted:.2f}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F = {converted:.2f}°C")
else:
    print("Invalid unit! Please enter C or F.")