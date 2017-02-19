from schedule_lib import schedule, controller
from datetime import timedelta
import datetime
import collections

class Console(object):
    def __init__(self, console_name, manager):
        self.console_name = console_name
        self.manager =  manager
        self.worked_schedule = {}
        self.scheduled = {}
        
        def add_scheduled_day(self,date, schedule_position):#schedule position just means ("","") or ("shift_one","shift_two")
            if schedule_position[0] != "" & schedule_position[0] != self.scheduled[date][0]:
                self.scheduled[date][0] = schedule_position[0]
            elif schedule_position[1] != "" & schedule_position[1] != self.scheduled[date][1]:
                self.scheduled[date][1] = schedule_position[1]
                
        def printschedule(self):
        #create ordered list of dictionary values
            ordered_schedule = collections.OrderedDict(sorted(self.scheduled.items()))
            for day in ordered_schedule:
                print(ordered_schedule[day])
                
        def controllers_on_shift(self, master_schedule, date):
            scheduled_shifts = master_schedule[date]
            
        
        
            
                
            