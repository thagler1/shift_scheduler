from schedule_lib import controller, functions, calendar, schedule, console
from testData import controllerinput as testdata
from testData import initialization as startup
import datetime
shift_list, controller_list, console_list = startup.initialize()

#test data to simulate PTO usage
controller_list[0].take_pto(75)
controller_list[0].add_oto(120)
controller_list[1].add_oto(120)
controller_list[2].add_oto(72)
controller_list[3].add_oto(24)

controller_list[3].add_consoles(('Seminole', '04/02/1990'))
#controller_list[3].set_primary_console('Seminole')
x = functions.lowman(controller_list)


master_schedule = functions.master_shift_schedule(shift_list, datetime.date(2017, 1, 1), datetime.date(2018, 12, 27))
day, night = console_list[1].controller_on_shift(master_schedule,datetime.date(2017,12,25),controller_list)
print(day.name)
print(night.name)
#print(console_list)





