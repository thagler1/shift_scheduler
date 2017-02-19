from schedule_lib import controller, functions, calendar, schedule
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
controller_list[3].set_primary_console('Seminole')
x = functions.lowman(controller_list)

print(x.info())
print(len(shift_list))

for console in console_list:
    print(functions.master_shift_schedule(shift_list, datetime.date(2017, 1, 1), datetime.date(2017, 2, 27)))