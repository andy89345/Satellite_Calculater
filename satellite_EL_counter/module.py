import math
from math import radians,cos,sin,asin,sqrt,degrees

class satellite_count:
    def __init__(self, vessel_lat,vessel_lon,satellite_lat,satellite_lon):
        self.vessel_lat=vessel_lat
        self.vessel_lon=vessel_lon
        self.satellite_lat=satellite_lat
        self.satellite_lon=satellite_lon

    def satellite_el(self):
        up=cos(radians(self.satellite_lon-self.vessel_lon))*cos(radians(self.vessel_lat))-0.15
        down=(1-(((cos(radians(self.satellite_lon-self.vessel_lon)))*cos(radians(self.vessel_lat))))**2)**0.5
        if down!=0:
            data=up/down
        else:
            data=0
        if data!=0:
            ans=degrees(math.atan(data))
        else:
            ans=degrees(math.atan(data))+90
   
        return round(ans,3)

    def satellite_AZ(self):

        up=math.tan(radians(self.satellite_lon-self.vessel_lon))
        down=math.sin(radians(self.vessel_lat))
        if down!=0:
            data=up/down
        else:
            data=0
        if ((self.satellite_lat-self.vessel_lat)>0) and ((self.satellite_lon-self.vessel_lon)>0):
            print("Satellite in I")
            ans=-degrees(math.atan(data))
        elif((self.satellite_lat-self.vessel_lat)>0) and ((self.satellite_lon-self.vessel_lon)<0):
            print("Satellite in II")
            ans=-degrees(math.atan(data))+360
        elif((self.satellite_lat-self.vessel_lat)<0) and ((self.satellite_lon-self.vessel_lon)<0):
            print("Satellite in III")
            ans=-degrees(math.atan(data))+180   
        elif((self.satellite_lat-self.vessel_lat)<0) and ((self.satellite_lon-self.vessel_lon)>0):
            print("Satellite in IV")
            ans=-degrees(math.atan(data))+180
        elif((self.satellite_lat-self.vessel_lat)==0) and ((self.satellite_lon-self.vessel_lon)>0):
            print("Satellite in east")
            ans=degrees(math.atan(data))+270
        elif((self.satellite_lat-self.vessel_lat)==0) and ((self.satellite_lon-self.vessel_lon)<0):
            print("Satellite in west")
            ans=degrees(math.atan(data))+90
        elif((self.satellite_lat-self.vessel_lat)>0) and ((self.satellite_lon-self.vessel_lon)==0):
            print("Satellite in north")
            ans=degrees(math.atan(data))
        elif((self.satellite_lat-self.vessel_lat)<0) and ((self.satellite_lon-self.vessel_lon)==0):
            print("Satellite in south")
            ans=degrees(math.atan(data))+180
        else:
            print("Satellite in Vessel position")
            ans=degrees(math.atan(data))
        return round(ans,3)

    def satellite_PA(self):
        up=sin(radians(self.satellite_lon-self.vessel_lon))
        down=math.tan(radians(self.vessel_lat))
        if down!=0:
            data=up-down
        else:
            data=0
        ans=degrees(math.atan(data))
        return round(ans,3)
        
    


