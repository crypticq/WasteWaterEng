import math


print("Welcome to the Coagulation Calculator")
print("This program will calculate the volume of the tank and the rate of dosing")
print(
    "This program will also calculate the retention time and the dimension of the tank"
)
print("This program will also calculate the actual retention time of the tank")
print("This program will also calculate the volume of the tank and each tank")
print("This program will also calculate the length and width of the tank")
print("This program will also calculate the dimension of the tank")
print("This program will also calculate the surface area of the tank")


ALUM_CONCENTRATION = 10
SPECIFIC_GRAVITY = 1


def volume_of_sol_tank(discahrge: int, dose: int, tanks: int, hours) -> float:
    """calculate the volume of the tank"""
    # 1. calculate the volume of the tank
    alum = (discahrge * dose) / 1000000
    volume_of_tank = (alum * 100) / (ALUM_CONCENTRATION * SPECIFIC_GRAVITY)
    print(f"volume of the tank is {volume_of_tank} / m3")
    print("Calculating the volume of each tank")
    volume_of_each_tank = volume_of_tank / tanks
    print(f"volume of each tank is {volume_of_each_tank} /m3")
    print("Calculating the rate of dosing")
    rate_of_dosing = volume_of_each_tank / hours

    rate_of_dosing_sec = rate_of_dosing / 3600
    print(f"rate of dosing is {rate_of_dosing} m3/hr")
    print(f"rate of dosing is {(rate_of_dosing_sec)} L/sec")


def design_tank(discharge: int, retention_time, dose: int, depth: int) -> float:
    print("Calculating retention time")
    capcity_of_tank = (discharge * retention_time) / 86400
    print(f"capacity of the tank is {round(capcity_of_tank)} m3")
    print("Calculating the volume of the tank")
    SAR = round(capcity_of_tank / depth)
    print(f"Surface Area is {SAR}")
    print("Calculating the length and width of the tank")
    length = round(math.sqrt(SAR))
    width = round(SAR / length)
    print(f"length of the tank is {length} m")
    print(f"width of the tank is {width} m")
    print("Calculating the dimension of the tank")
    volume_of_tank = length * width * depth
    Actul_retention_time = (volume_of_tank / discharge) * 24 * 3600
    print(f"Actual retention time is {round(Actul_retention_time)} Days")


if __name__ == "__main__":
    discharge = int(input("Enter the discharge of the plant in L/sec: "))
    dose = int(input("Enter the dose of the plant in mg/L: "))
    retention_time = int(input("Enter the retention time of the plant in Days: "))
    depth = int(input("Enter the depth of the tank in m: "))
    hours = int(input("Enter the hours of the plant in Hours: "))
    tanks = int(input("Enter the number of tanks: "))
    volume_of_sol_tank(discharge, dose, tanks, hours)
    design_tank(discharge, retention_time, dose, depth)
