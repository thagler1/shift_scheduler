########################################################################################
#Purpose: initialize program with test data. Eventually this will initialize with DB data
#Input: hardcoded shift state information, and controller information
#Author: Todd Hagler
#Date: 2/19/2017
#Last Modified: 2/19/17
#######################################################################################
from schedule_lib import controller, functions, calendar, schedule, console
from testData import controllerinput as testdata
#initialize empty list for storing controller objects in


def initialize():
    controller_list = []
    console_list = []
    
    #initialize shift schedule
    shift_id = ['one','two','three','four']
    offsets = {'one': 17, 'two':10, 'three':3, 'four':24}
    shift_list = [schedule.Schedule(shift, offsets[shift]) for i, shift in enumerate(shift_id)]
    
    #Initialize Consoles
    for desk in testdata.consoles:
        newconsole = console.Console(desk['name'], desk['manager'])
        console_list.append(newconsole)


        
    
    
    for i, employee in enumerate(testdata.controllers):
        new = controller.Controller(employee['name'], employee['consoles'])
        new.set_shift(functions.identify_shift(employee['shift'], shift_list))#function to assign shift object to controller.shift
        new.set_rate(employee['rate'])
        new.set_pto(employee['pto'])
        new.set_manager(employee['manager'])
        new.set_primary_console(employee['primary_console'])
        
        
        controller_list.append(new)

    return shift_list, controller_list, console_list
