boil_temperature = int(input())

atmospheric_pressure = 5 * boil_temperature - 400

sea_level = 1

if atmospheric_pressure == 100:
    sea_level = 0
elif atmospheric_pressure > 100:
    sea_level = -1

print(atmospheric_pressure)
print(sea_level)
