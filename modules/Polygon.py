class Polygon:
    def __init__(self):
        self.type = "Feature"
        self.geometryType = "Polygon"
        self.coordinates = []
        self.properties = {}

    def addCoordinate(self, coordinate):
        self.coordinates.append(coordinate)

    def addProperty(self, property, value):
        self.properties[property] = value

    def dictToString(self):
        dictString = ""
        for property in self.properties:
            dictString += f"\n\t\t\t\t\"{property}\": \"{str(self.properties[property])}\","
        dictString = dictString.rstrip(",")
        return dictString

    def toString(self):
        origin = self.coordinates[0]
        self.coordinates.append(origin)
        coords = ",\n\t\t\t\t\t\t".join(self.coordinates)
        props = self.dictToString()
        result = "{\n\t\t\t\"type\": \"Feature\",\n\t\t\t\"geometry\": {\n\t\t\t\t\"type\": \"Polygon\",\n\t\t\t\t\"coordinates\": [\n\t\t\t\t\t[\n\t\t\t\t\t\t" + \
            coords + \
            "\n\t\t\t\t\t]\n\t\t\t\t]\n\t\t\t},\n\t\t\t\"properties\":{" + \
            props + "\n\t\t\t}\n\t\t}"
        self.coordinates.clear()
        return result
