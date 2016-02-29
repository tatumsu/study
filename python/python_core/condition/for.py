#!/usr/bin/env python
# -*- coding: utf -*-
class Train(object):
    def __init__(self, cars):
        print "__init__ is invoked"
        self.cars = cars

    def __len__(self):
        print "__len__ is invoked"
        return self.cars
    
    def __getitem__(self, key):
        print "__getitem__ is invoked with index %s" % key
        if key >= 0:
            index = key
        else:
            index = self.cars + key
   
        #len(self) 
        if 0 <= index < len(self.cars):
            return 'Carriage %s' % (self.cars[key])
        else:
            raise IndexError('No carriage at %s' % key)
    
    #def __iter__(self):
    #    print "__iter__ is invoked"
    #    return iter(self.cars)

t=Train(['CAR1', 'CAR_RED', 'CAR_WHITE', 'FOX', 'BIG'])
#t=Train(4)
for car in t:
    print car
