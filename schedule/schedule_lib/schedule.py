import datetime
from datetime import timedelta
import collections

class Schedule(object):
    #Hardcoded shift info, this can be bypassed. 
    
    
    
    shift_id = ['one','two','three','four']
    offsets = {'one': 17, 'two':10, 'three':3, 'four':24}
    
    n = "Night"
    d = "Day"
    o = "off"
    dupont = [n, n, n, n, o, o, o, d, d, d, o, n, n, n, o, o, o, d, d, d, d, o, o, o, o, o, o, o]
    len(dupont)
    
    def addshift(self, sequence, shiftname, schedule):
    
        for i, shift in enumerate(sequence):
            date_count = self.startdate + datetime.timedelta(days=i)
            #print(date_count)
            #print(type(date_count))
            if shift == "Day":
                schedule[date_count][0] = self.shift_id
                
            elif shift == "Night":
                schedule[date_count][1] = self.shift_id
                
            else:
                pass
        return schedule
    
    
    def buildshift(self):
        sequence = []
        full_sequence = []
        schedule = {self.startdate + datetime.timedelta(days =x):["",""]for x in range(self.year)} 

        for shift in self.rotation[self.zeroday - 1:]:
            sequence.append(shift)
        for shift in self.rotation[:self.zeroday - 1]:
            sequence.append(shift)
        while len(full_sequence) < self.year:
            for shift in sequence:
                full_sequence.append(shift)

        self.addshift(full_sequence[:self.year], self.shift_id, schedule)
        return schedule
    
    def __init__(self, shift_id, zeroday, rotation = dupont):
        self.startdate = datetime.date(2017,1, 1)  #year, month, day
        self.enddate = datetime.date(2020,1,1)
        self.span = (self.enddate - self.startdate)
        self.year = self.span.days
        self.rotation = rotation
        self.shift_id = shift_id
        self.zeroday = zeroday
        self.schedule = self.buildshift()
      
    def shiftname(self):
        return self.shift_id

    
    def printschedule(self):
        #create ordered list of dictionary values
        ordered_schedule = collections.OrderedDict(sorted(self.schedule.items()))
        for day in ordered_schedule:
            print(ordered_schedule[day])
        
    def date_check(self, year, month, day):
    #check to see if a shift is scheduled for a specific day. Returns dupont posistion
        check_date = datetime.date(year, month, day)  #year, month, day
        return (self.schedule[check_date])

    def check_date(self, date):
        return self.schedule[date]
