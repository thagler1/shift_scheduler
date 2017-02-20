from datetime import timedelta
import datetime
import collections

class Console(object):
    def __init__(self, console_name, manager):
        self.console_name = console_name
        self.manager =  manager
        self.worked_schedule = {}
        self.scheduled = {}
        
    def add_scheduled_day(self,date, schedule_position):# schedule position just means ("","") or
        # ("shift_one","shift  _two")
        if schedule_position[0] != "" and schedule_position[0] != self.scheduled[date][0]:
            self.scheduled[date][0] = schedule_position[0]
        elif schedule_position[1] != "" and schedule_position[1] != self.scheduled[date][1]:
            self.scheduled[date][1] = schedule_position[1]

    def printschedule(self):
    #create ordered list of dictionary values
        ordered_schedule = collections.OrderedDict(sorted(self.scheduled.items()))
        for day in ordered_schedule:
            print(ordered_schedule[day])

    def controller_on_shift(self, master_schedule, date, controller_list):
        # Check the master shift schedule for which shift is working that day, then find the controller on that
        # shift with that desk as the primary console
        scheduled_shifts = master_schedule[date]
        print(scheduled_shifts)
        possible_controller =[]
        for controller in controller_list:
            if controller.shift.shift_id == scheduled_shifts[0] and controller.primary_console == self.console_name:
                dayshift = controller
            elif controller.shift.shift_id == scheduled_shifts[1] and controller.primary_console == self.console_name:
                nightshift = controller
        return (dayshift, nightshift)



            
        
        
            
                
            