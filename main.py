"""
Main

Main script to plot my coffee intake 
"""

import numpy
from matplotlib import pyplot
import pandas

import utils

defaultScheme = 'bright'

figArgs = {'figsize': (16.0, 9.0)}

data = pandas.read_csv('coffee-tracker.csv', parse_dates=[[0, 1, 2, 3, 4]], header=None,
                       date_parser=utils.dateParser)
data.columns = ['Datetime', 'Drink', 'Location', 'City', 'State']
data['date'] = pandas.Series([xx.date() for xx in data.Datetime])
data['dateNum'] = pandas.Series([(xx.date() - data.Datetime[0].date()).days for xx in data.Datetime])
data['timeNum'] = pandas.Series([xx.hour + xx.minute / 60. for xx in data.Datetime])

uniqueDrinks = data.Drink.unique()
data['drinkID'] = pandas.Series([numpy.where(xx == uniqueDrinks)[0][0] for xx in data.Drink])

# plot total drink consumption
dayFig, dayAx = pyplot.subplots(1, 1, **figArgs)
data.plot.scatter('dateNum', 'timeNum', ax=dayAx)
utils.formatAxis(dayAx, x='date', y='time')

# plot number of drinks per day
numDrinksFig, numDrinksAx = pyplot.subplots(1, 1, **figArgs)
data.dateNum.value_counts().plot.hist(ax=numDrinksAx)
numDrinksAx.set_xlabel('Number of drinks per day')
numDrinksAx.set_ylabel('Frequency')

if __name__ == '__main__':
    pyplot.show()