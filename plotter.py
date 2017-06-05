"""
Plotter

Routines for plotting and manipulating coffee tracker data

"""

from matplotlib import pyplot
from matplotlib.dates import num2date
from seaborn import color_palette

import Drinks
import utils

def getData():
    """Read the data from csv file and return list of coffee objects."""
    return utils.csvToList('coffee-tracker.csv', utils.createObjects)


def plotDOYvsTime(ax, data, colorBy, colorScheme='bright'):
    """
    Plot base types of coffee consumption for days of the year vs. time.

    Parameters
    ----------
    ax: matplotlib.axes._subplots.AxesSubplot
        subplot window to which the data will be added
    data: list
        list of Drink objects

    """

    daysOfYear = _getDaysOfYear(data)
    drinkTimes = [datum.time2Num() for datum in data]
    plotColors = _getColors(data, colorBy, colorScheme)

    ax.scatter(daysOfYear, drinkTimes, c=plotColors)

    _setXTicksFormattedDays(ax, data)
    _setYTicksSingleDayTimes(ax)
    
    
def plotNumberDrinksPerDay(ax, data):
    """
    Plot the number of drinks per day.
    
    Parameters
    ----------
    ax: matplotlib.axes._subplots.AxesSubplot
        subplot window to which the data will be added
    data: list
        list of Drink objects
    
    """
    
    daysOfYear, numDrinks = _getNumDrinksPerDay(data)
    
    ax.plot_date(daysOfYear, numDrinks, 'o')
    ax.set_xlabel('Day')    
    ax.set_ylabel('Number of drinks per day')


def _getColors(data, colorBy, colorScheme):
    if colorBy == 'base':
        return _getBaseColors(data, colorScheme)
    elif colorBy == 'unique':
        return _getUniqueColors(data, colorScheme)
    else:
        raise KeyError('Need either unique or base for colorBy, not {}'.format(colorBy))


def _setYTicksSingleDayTimes(ax):
    pyplot.yticks((6.0, 9.0, 12.0, 15.0, 18.0, 21.0),
                  ('6 am', '9 am', '12 pm', '3 pm', '6 pm', '9 pm'))
    ax.set_ylabel('Local Time')

def _setXTicksFormattedDays(ax, data):
    `
    pyplot.xticks(xlocs, xlabels, rotation=17)
    ax.set_xlabel('Day')

def _getPalette(colorScheme, numItems):
    return color_palette(colorScheme, numItems)

def _getUniqueColors(data, colorScheme):
    listedDrinks = Drinks.allDrinks()
    palette = _getPalette(colorScheme, len(listedDrinks))
    return [palette[listedDrinks.index(datum.drinkClass())] for datum in data]

def _getBaseColors(data, colorScheme):
    mainDrinks = Drinks.mainTypes()
    palette = _getPalette(colorScheme, len(mainDrinks))
    return [palette[mainDrinks.index(datum.baseType())] for datum in data]

def _getDaysOfYear(data):
    dayZeroObject = min(data, key = lambda item: item.date)
    dayZeroOffset = dayZeroObject.date2Num()
    return [datum.date2Num() - dayZeroOffset for datum in data]
    
def _getNumDrinksPerDay(data):
    numVec = []
    dayVec = []
    dayCount = 1
    totalNumber = len(data)
    for nn, drink in enumerate(data):
        if nn == totalNumber - 1:
            numVec.append(dayCount)
            return dayVec, numVec 
            
        if dayCount == 1:
            date = drink.date
            dayVec.append(date)
            
        if data[nn + 1].date == date:
            dayCount += 1
        else:
            numVec.append(dayCount)
            dayCount = 1       
        