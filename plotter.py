"""
Plotter

Routines for plotting and manipulating coffee tracker data

"""

from datetime import datetime

from matplotlib import pyplot
from matplotlib.dates import date2num
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
    plotColors = _colorByFuncSwitcher(colorBy, _getBaseColors, _getUniqueColors, 
                                      [data, colorScheme])

    ax.scatter(daysOfYear, drinkTimes, c=plotColors)
    #_setLegend(ax, colorBy, colorScheme)

    _setXTicksFormattedDays(ax, data)
    _setYTicksSingleDayTimes(ax)
    return ax
    
    
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


def _setYTicksSingleDayTimes(ax):
    pyplot.yticks((6.0, 9.0, 12.0, 15.0, 18.0, 21.0),
                  ('6 am', '9 am', '12 pm', '3 pm', '6 pm', '9 pm'))
    ax.set_ylabel('Local Time')

def _setXTicksFormattedDays(ax, data):
    firstOffset = _firstDrink(data).date2Num()
    months = _monthsBetween(data)
    locs = [date2num(month) - firstOffset for month in months]
    labels = [month.strftime('%Y-%m') for month in months]
    pyplot.xticks(locs, labels)
    ax.set_xlabel('Day')
    
def _setLegend(ax, colorBy, colorScheme):
    #TODO create patch objects off of the colors in palette
    if colorBy == 'base':
        legendItems = Drinks.mainTypes()
    elif colorBy == 'unique':
        legendItems = Drinks.allDrinks()
    else:
        raise KeyError('Need unique or base for colorBy, not {}'.format(colorBy))
    
    numItems = len(legendItems) 
    palette = _getPalette(colorScheme, numItems)
    h = [palette[indx] for indx in range(numItems)]
    l = [str(indx) for indx in range(numItems)]
    print(h, l, end='\n')
    ax.legend(handles=h, labels=l)      
        
        
def _colorByFuncSwitcher(colorBy, baseFunc, uniqueFunc, args):
    if colorBy == 'base':
        return baseFunc(*args)
    elif colorBy == 'unique':
        return uniqueFunc(*args)    
    else:
        raise KeyError('Need unique or base for colorBy, not {}'.format(colorBy))
       

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
    dayZeroOffset = _firstDrink(data).date2Num()
    return [datum.date2Num() - dayZeroOffset for datum in data]
    
def _firstDrink(data):
    return min(data, key=lambda drink: drink.dateTime)
        
def _lastDrink(data):
    return max(data, key=lambda drink: drink.dateTime)        
    
def _monthsBetween(data):
    first = _firstDrink(data).dateTime
    last = _lastDrink(data).dateTime
    return [datetime.strptime('{}-{}'.format(yy, mm), '%Y-%m') 
            for mm in range(first.month, last.month + 1)
            for yy in range(first.year, last.year + 1)]
            
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
        