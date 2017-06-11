"""
Utilities for creating/plotting data

"""

from datetime import datetime

def dateParser(*args):
    return datetime.strptime('-'.join([str(xx) for xx in args]), '%y-%m-%d-%H-%M')
    
def formatAxis(ax, x='date', y='time'):
    funcs = {'date': _formatAxis_date, 'time': _formatAxis_time}
    if x in funcs:
        funcs[x](ax)
    if y in funcs:
        funcs[y](ax)            
    
def _formatAxis_date(ax):
    ax.set_xlabel('Date')
    
def _formatAxis_time(ax):
    ax.set_ylabel('Local Time')        
    # more methods for setting ticks