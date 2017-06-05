"""
Main

Main script to plot my coffee intake 
"""

from matplotlib import pyplot

import plotter

defaultScheme = 'bright'

figArgs = {'figsize': (16.0, 9.0)}

data = plotter.getData()

daysVsTypeFig, dayVsTimeAx = pyplot.subplots(1, 1, **figArgs)
plotter.plotDOYvsTime(dayVsTimeAx, data, colorBy='base', colorScheme=defaultScheme)

if __name__ == '__main__':
    pyplot.show()