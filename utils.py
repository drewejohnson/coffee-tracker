"""


"""             
import csv

import Drinks


ESPRESSO_DRINKS = ['espresso', 'flat white', 'mocha', 'cappucino']
COFFEE_DRINKS = ['drip', 'french press', 'siphon', 'aeropress']

def csvToList(filePath, formatFunc):
    """Return the data from keepFile filePath."""
    data = []
    with open(filePath, 'r', newline='') as csvObj:
        reader = csv.reader(csvObj, delimiter=',')
        for line in reader:
            data.append(formatFunc(cleanLine(line)))
    return data
    

def formatKeepLine(line, defaultCity=('Atlanta', 'GA')):
    """Reformat the data in keep formatted line."""
    addDefaultCity(line, 8, defaultCity)
    if line[5] == 'pm':
        line[3] = str(int(line[3]) + 12)
    del line[5] 
    return line     
    

def formatDocsLine(line, defaultCity=('Atanta', 'GA')):
    """Reformat the data from the original Google Docs format."""
    line[5], line[6] = line[6], line[5]
    addDefaultCity(line, 7, defaultCity)
    return line
    

def createCoffeeObjs(line):
    """Return an instance of Drink corresponding to the data in this line."""
    dateTime = line[:5]
    location = line[6:]
    drinkType = line[5]
    if drinkType in ESPRESSO_DRINKS:
        return Drinks.Espresso(dateTime, drinkType, location)
    elif drinkType in COFFEE_DRINKS:
        return Drinks.Coffee(dateTime, drinkType, location)
    else:
        return Drinks.Other(dateTime, drinkType, location)       
    
def cleanLine(lineList):
    return [val.strip() for val in lineList if val]


def addDefaultCity(lineList, shortLen, defaultCity):
    if len(lineList) == shortLen:
        lineList.extend(defaultCity)


def _writecsv(outFile, data):
    with open(outFile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for coffeeObj in data:
            writer.writerow(coffeeObj.toCsv())

def writeListOfDrinks(outFile, data):
    writeData = sorted(data, key=lambda coffeeObj: coffeeObj.dateTime)
    _writecsv(outFile, writeData)