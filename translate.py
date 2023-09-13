import argparse
import os

from modules.Coordinate import Coordinate
from modules.CSVHandler import CSVHandler
from modules.FileHandler import FileHandler
from modules.GeoJSON import GeoJSON
from modules.Polygon import Polygon


def findHeader(headerString, fileArray):
    for num, line in enumerate(fileArray):
        Polygon = line.rstrip()
        if Polygon.startswith(headerString):
            return num
    return None


def readFile(sourceDir, outputDir, sourceFile, outputFile, headerLine):
    fileHandler = FileHandler()
    print("\nChecking for Old Files")
    fileHandler.checkDir(outputDir)
    fileHandler.deleteAllInSubdir(".geojson", outputDir)
    fileHandler.deleteAllInSubdir(".csv", outputDir)
    print("\nReading Source File")
    with open(sourceDir + "/" + sourceFile, 'r') as dataFile:
        fileData = dataFile.readlines()
    headerLineNumber = findHeader(headerLine, fileData)
    if headerLineNumber != None:
        with open(outputDir + "/" + sourceFile, 'w') as tempFile:
            tempFile.writelines(fileData[headerLineNumber:])
        csvFile = CSVHandler(outputDir + "/" + sourceFile)
        csvData = csvFile.toDict()
        jsonData = GeoJSON()
        for line in csvData:
            if line['Coordinates'] != "":
                l = Polygon()
                l.addProperty("facility", line['Owning Facility'])
                l.addProperty("favId", line['Fav Id'])
                l.addProperty("minAlt", line['Min Alt'])
                l.addProperty("maxAlt", line['Max Alt'])
                coords = line['Coordinates'].split('  ')
                for coord in coords:
                    c = Coordinate()
                    latD = int(coord[0:2])
                    latM = int(coord[2:4])
                    latS = int(coord[4:8])/100
                    latD = -latD if coord[8:9] == "S" else latD
                    lonD = int(coord[10:13])
                    lonM = int(coord[13:15])
                    lonS = int(coord[15:19])/100
                    lonD = -lonD if coord[20:21] == "W" else lonD
                    c.fromDMS(latD, latM, latS, lonD, lonM, lonS)
                    l.addCoordinate(c.toString())
                jsonData.addFeature(l.toString())
        jsonOutput = jsonData.toString()
        if os.path.exists(outputDir + "/" + outputFile):
            os.remove(outputDir + "/" + outputFile)
        with open(outputDir + "/" + outputFile, 'w') as resultFile:
            resultFile.writelines(jsonOutput)


def main():
    # Set up Defaults
    SOURCE_DIR = "source"
    OUTPUT_DIR = "output"
    OUTPUT_FILE = "fav.json"
    HEADER_LINE = "Fav Id,Owning Facility,Type,Module Id,Min Alt,Max Alt,Coordinates"
    # Set up Argument Handling
    parser = argparse.ArgumentParser(description="FAV-Translator")
    parser.add_argument("--filename", type=str,
                        help="The filename of the FAV file.")
    args = parser.parse_args()
    if args.filename != None:
        print(f"Using filename {args.filename}")
        readFile(SOURCE_DIR, OUTPUT_DIR, args.filename,
                 OUTPUT_FILE, HEADER_LINE)

    else:
        print(">>> Please set the filename with the --filename flag")


if __name__ == "__main__":
    main()
