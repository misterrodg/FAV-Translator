class Coordinate:

    def __init__(self, lat=0.0, lon=0.0):
        self.lat = lat
        self.lon = lon

    def fromDMS(self, latD, latM, latS, lonD, lonM, lonS):
        self.lat = latD + (latM / 60) + (latS / (60*60))
        self.lon = -lonD - (lonM / 60) - (lonS / (60*60))

    def toString(self):
        result = "[" + str(self.lon) + ", " + str(self.lat) + "]"
        return result
