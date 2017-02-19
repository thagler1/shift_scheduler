###############################################################################################################
#Purpose: Create controller object and manage all functions related to it
#input: name, shift, rate, pto, managers,consoles
#Author: Todd Hagler
#Date:2/19/17
################################################################################################################
import sys
from schedule_lib import schedule

class Controller(object):
    
    def __init__(self, name="", consoles = {}, shift = 9, rate = 0, pto = 0, manager = "" , primary_console = ""):
        self.name = name
        self.shift =shift
        self.rate = rate
        self.pto = pto
        self.manager = manager
        self.consoles = consoles
        self.primary_console = primary_console #Currently hardcoded in the controller input. might be a better way
        self.oto = 0
        self.pto_dates =[]
        self.ot_dates_scheduled = []#Future dates and shifts scheduled to work
        self.ot_dates_worked = []#archive of dates worked.
   
    def set_shift(self, shift):
        self.shift = shift
        
    def set_rate(self, rate):
        #change rate of controller
        self.rate = rate
    
    def set_pto(self, pto):
        #change current PTO amount. 
        self.pto = pto
    
    def set_manager(self, manager):
        #assign new manager to controller
        self.manager = manager
        
    def add_consoles(self, console):
        #console = ('Console name', 'date oq'd) adds new console to controller
        self.consoles[console[0]] = console[1]
        
    def take_pto(self, pto):
        self.pto -= pto
        
    def add_oto(self, oto):
        self.oto += oto
    def set_primary_console(self, console_name):
        self.primary_console = console_name
        
    def add_pto_dates(self, pto_start, pto_end):
        # add each individual shift to pto range
        #/todo add each date in range for pto
        self.pto_dates.append(pto_dates)
        
    def qualified(self, desk):
        if desk in self.consoles:
            return False
        else:
            return True
    def names(self):
        print(self.name)
    
    def info(self):
        print("Name : "+ self.name)
        print("Shift : "+str(self.shift.shiftname()))
        print("PTO : "+ str(self.pto))
        print("Manager : " +self.manager)
        print("Consoles : " + str(self.consoles))
        print("Primary Console : " + self.primary_console)
        print("Over Time Offered : "+str(self.oto))

        

    def check_date(self, year, month, day):
        result = self.shift.date_check(year, month, day)
        return result
        


        
        
