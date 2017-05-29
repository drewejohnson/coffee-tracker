"""

"""
from datetime import datetime


class Drink(object):
    
    _timeDelim = '-'
    _timeItems = ['%y', '%m', '%d', '%H', '%M']
    timeFormat = _timeDelim.join(_timeItems)
    
    def __init__(self, dateTime, drinkType, location):
        self.dateTime = self.formatTime(dateTime)
        self.drinkType = drinkType
        self.location = location
        
    def formatTime(self, dateTimeVec):
        """Convert the dateTime iterable into a datetime object.
        
        Returns
        -------
            dateTime: datetime instance
            
        Notes
        -----
        The dateTimeVec iterable format is (YY, MM, DD, HH, mm)
        All times are local
        """
        timeStr = self._timeDelim.join([val.zfill(2) for val in dateTimeVec])
        return datetime.strptime(timeStr, self.timeFormat)
    
    
    def __str__(self):
        return '{} from {}'.format(self.__class__.__name__,
                                   self.dateTime.strftime(self.timeFormat))
                                   
    def toCsv(self, delims=_timeItems):
        timeVec = [self.dateTime.strftime(dd) for dd in delims]
        timeVec.append(self.drinkType)
        timeVec.extend(self.location)
        return timeVec
        
        
        
class Coffee(Drink):        
    def __init__(self, dateTime, drinkType, location):
        Drink.__init__(self, dateTime, drinkType, location)
        
        
class Espresso(Drink):
    def __init__(self, dateTime, drinkType, location):
        Drink.__init__(self, dateTime, drinkType, location)


class Other(Drink):
    def __init__(self, dateTime, drinkType, location):
        Drink.__init__(self, dateTime, drinkType, location)        