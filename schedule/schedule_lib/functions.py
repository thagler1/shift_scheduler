#####################################################################################
#Purpose: Repo for functions that do not fall under class
#input: varies per function
#Author: Todd Hagler
#Date: 2/19/17
#Last Modified: 2/19/17
#####################################################################################
from datetime import timedelta
import datetime
import collections

def lowman(controller_list):
    #returns controller with lowest OTO
    #pass a list of controller objects and return the low man as a controller object
    lowmanname = ""
    lowmanoto = 1000
    lowman = ""
    highmanoto = 0
    highman = ""
    no_oto = False
    for controller in controller_list:
        if controller.oto < lowmanoto:
            lowmanoto = controller.oto
            lowmanname = controller.name
            lowman = controller
        if controller.oto >= highmanoto:
            highmanoto = controller.oto
            highman = controller
    
    if highmanoto == 0:
        no_oto = True
        return no_oto

    
    return lowman
    

def qualified_controllers(desk, controller_list):
    oq = []
    for controller in controller_list:
        if controller.qualified(desk) == False:
            oq.append(controller)
        
    return oq
    #check to see if a shift is scheduled to work on a certain day. Return shift value
    #day needs to be in [year, day, month]
    
    
def identify_shift(shiftname, shift_list):
    #this is for finding a specific shift object and assigning it to a controller
    #this should probably throw an error
    for shift in shift_list:
        if shift.shiftname() == shiftname:
            return shift
'''          
def desk_shift_schedule(shift_list, start_date, end_date, console):
    #this is a list of dicts that will tell you which shift is working which days
    startdate = datetime.date(start_date)  #year, month, day
    enddate = datetime.date(end_date)
    span = (self.enddate - self.startdate) 
    schedule_range = {(startdate + datetime.timedelta(days =x),"","")for x in range(span)}
    for desk in console:
        for shift in shift_list:
            for day in schedule_range:
                x = shift.date_check(day)
                if x != ["",""]:
                    desk.add_scheduled_day(day, x)
'''                    
def master_shift_schedule(shift_list, start_date, end_date):
    #this is a list of dicts that will tell you which shift is working which days

    span = (end_date - start_date)
    timeframe = span.days
    master_schedule = {start_date + datetime.timedelta(days =x):["",""]for x in range(timeframe)}
    ordered_schedule = collections.OrderedDict(sorted(master_schedule.items()))
    
    for shift in shift_list:
        for day in ordered_schedule:
            x = shift.check_date(day)
            dayshift = ""
            nightshift = ""
            if x[0] != "":
                dayshift = shift.shiftname()
                master_schedule[day][0] = dayshift 
            if x[1] != "":
                nightshift = shift.shiftname()
                master_schedule[day][1] = nightshift
            else:
                pass
            
    return master_schedule


    

        