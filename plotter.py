"""
Plotter

Routines for plotting and manipulating coffee tracker data

"""

from matplotlib import pyplot

import Drinks
import utils

def getData():
    """Read the data from csv file and return list of coffee objects."""
    return utils.csvToList('coffee-tracker.csv', utils.createObjects)
    
    
def plotDOYvsTime(ax, data):
    """
    Plot base types of coffee consumption for days of the year vs. time.
    
    Parameters
    ----------
    ax: matplotlib.axes._subplots.AxesSubplot
        subplot window to which the data will be added
    data: list
        list of Drink objects with date2Num, time2Num, and baseColor objects
        
    """
    
    daysOfYear = [datum.date2Num() for datum in data]
    drinkTimes = [datum.time2Num() for datum in data]
    plotColors = [datum.baseColor for datum in data]
    
    ax.scatter(daysOfYear, drinkTimes, color=plotColors)
    # set the x axis ticks with pyplot.xticks() then num2date and reformat
    # set the y axis ticks with pyplot.yticks() and then reformat....
    return ax