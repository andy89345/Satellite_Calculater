import math
from math import radians,cos,sin,asin,sqrt,degrees
from module import satellite_count
from pyfiglet import Figlet
f = Figlet(width=2000)
print(f.renderText("LH Satellite counter"))
print("------------------------------")
print("Author : Andy Lin            |")
print("Last Update : 2022/08/18     |")
print("------------------------------\n\n")
while True:
    print("============================")
    satellite_lat=float(input("satellite_lat : "))
    satellite_lon=float(input("satellite_lon : "))
    vessel_lat=float(input("vessel_lat : "))
    vessel_lon=float(input("vessel_lon : "))
    satellite=satellite_count(vessel_lat,vessel_lon,satellite_lat,satellite_lon)
    EL=satellite.satellite_el()
    AZ=satellite.satellite_AZ()
    PA=satellite.satellite_PA()
    print(f"AZ : {AZ}")
    print(f"EL : {EL}")
    print(f"PA : {PA}")
    print("============================\n\n")