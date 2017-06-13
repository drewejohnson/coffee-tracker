"""
Main

Main script to plot my coffee intake
"""

from matplotlib import pyplot
import pandas
import seaborn

import utils

seaborn.set(style='dark')
chosenPalette = 'Set2'

data = pandas.read_csv('coffee-tracker.csv', header=None,
                       parse_dates=[[0, 1, 2, 3, 4]],
                       date_parser=utils.dateParser)
data.columns = ['Datetime', 'Drink', 'Location', 'City', 'State']
data['date'] = pandas.Series([xx.date() for xx in data.Datetime])
data['dateNum'] = pandas.Series([(xx.date() - data.Datetime[0].date()).days
                                 for xx in data.Datetime])
data['Local Time'] = pandas.Series([xx.hour + xx.minute / 60.
                                   for xx in data.Datetime])
data['weekday'] = pandas.Series([xx.weekday_name for xx in data.Datetime])
data['Day of Week'] = pandas.Series([xx.dayofweek for xx in data.Datetime])

# plot total drink consumption
def plotTotal(df):
    dayFig, dayAx = pyplot.subplots(1, 1, **figArgs)
    groupedDrinks = df.groupby('Drink')
    for key, group in groupedDrinks:
        group.plot(x='dateNum', y='Local Time', kind='scatter',
                   ax=dayAx, label=key)
    utils.formatAxis(dayAx, x='date', y='time')

# plot number of drinks per day
def plotNumDay(df):
    numDrinksFig, numDrinksAx = pyplot.subplots(1, 1, **figArgs)
    df.dateNum.value_counts().plot.hist(ax=numDrinksAx)
    numDrinksAx.set_xlabel('Number of drinks per day')
    numDrinksAx.set_ylabel('Frequency')

if __name__ == '__main__':
    # Plot day of the week vs time of Drink
    ax = seaborn.swarmplot(data=data, x='Day of Week', y='Local Time',
                           order=['Sunday','Monday','Tuesday','Wednesday',
                          'Thursday','Friday','Saturday'], hue='Drink',
                          palette=chosenPalette)
    ax.legend(ncol=4)

    ax = seaborn.countplot(data=data, x='dateNum',
                           palette=seaborn.color_palette(chosenPalette, 1))
    ax.set_ylabel('Drinks per day')

    pyplot.show()