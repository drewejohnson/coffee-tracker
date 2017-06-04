"""

"""
from datetime import datetime

from matplotlib.dates import date2num

class _Drink(object):

    timeDelim = '-'
    timeItems = ['%y', '%m', '%d', '%H', '%M']
    timeFormat = timeDelim.join(timeItems)

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
        timeStr = self.timeDelim.join([val.zfill(2) for val in dateTimeVec])
        return datetime.strptime(timeStr, self.timeFormat)


    def __str__(self):
        return '{} from {}'.format(self.__class__.__name__,
                                   self.dateTime.strftime(self.timeFormat))

    def toCsv(self, delims=timeItems):
        timeVec = [self.dateTime.strftime(dd) for dd in delims]
        timeVec.append(self.drinkType)
        timeVec.extend(self.location)
        return timeVec
        
    @property
    def time(self):
        return self.dateTime.time()
        
    @property
    def date(self):
        return self.dateTime.date()
        
    def time2Num(self):
        return self.time.hour + self.time.minute / 60.    
        
    def date2Num(self):
        return date2num(self.date)


class _Drip(_Drink):
    def __init__(self, dateTime, drinkType, location):
        _Drink.__init__(self, dateTime, drinkType, location)
        self.baseColor = '#aa3939'


class _Espresso(_Drink):
    def __init__(self, dateTime, drinkType, location):
        _Drink.__init__(self, dateTime, drinkType, location)
        self.baseColor = '#aa6C39'


class _Other(_Drink):
    def __init__(self, dateTime, drinkType, location):
        _Drink.__init__(self, dateTime, drinkType, location)
        self.baseColor = '#226666'


class Drip(_Drip):
    def __init__(self, dateTime, location):
        _Drip.__init__(self, dateTime, 'drip', location)


class Siphon(_Drip):
    def __init__(self, dateTime, location):
        _Drip.__init__(self, dateTime, 'siphon', location)


class PourOver(_Drip):
    def __init__(self, dateTime, location):
        _Drip.__init__(self, dateTime, 'pour over', location)

class FrenchPress(_Drip):
    def __init__(self, dateTime, location):
        _Drip.__init__(self, dateTime, 'french press', location)


class ColdBrew(_Drip):
    def __init__(self, dateTime, location):
        _Drip.__init__(self, dateTime, 'cold brew', location)


class Aeropress(_Drip):
    def __init__(self, dateTime, location):
        _Drip.__init__(self, dateTime, 'aeropress', location)
        
        
class IcedCoffee(_Drip):
    def __init__(self, dateTime, location):
        _Drip.__init__(self, dateTime, 'iced coffee', location)        


class Mocha(_Espresso):
    def __init__(self, dateTime, location):
        _Espresso.__init__(self, dateTime, 'mocha', location)


class Latte(_Espresso):
    def __init__(self, dateTime, location):
        _Espresso.__init__(self, dateTime, 'latte', location)


class FlatWhite(_Espresso):
    def __init__(self, dateTime, location):
        _Espresso.__init__(self, dateTime, 'flat white', location)


class Cappuccino(_Espresso):
    def __init__(self, dateTime, location):
        _Espresso.__init__(self, dateTime, 'cappuccino', location)


class Espresso(_Espresso):
    def __init__(self, dateTime, location):
        _Espresso.__init__(self, dateTime, 'espresso', location)


class FourSigThink(_Other):
    def __init__(self, dateTime, location):
        _Other.__init__(self, dateTime, 'four sigmatic think', location)