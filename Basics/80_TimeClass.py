''' 
TimeClass:
class datetime.time(hour=0, minute=0,second=0,microsecond=0,tzinfo=None,*,fold=0)

tzinfo can be None otherwise all the atributes must be an integer.
'''

from datetime import time 

mintime=time.min 
print("Min Time supprted",mintime)
maxtime=time.max
print("Max Time supprted",maxtime)

time=time(12,12,12,1212)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

from datetime import time 
time1 = time(12, 36, 24, 2022)
str1 = time1.isoformat()
print(str1)
print(type(str1))

time_string = "12:24:36.001212"
time2 = time.fromisoformat(time_string)
print("Time from string:", time2)
print(type(time2))

time3=time(12,24,36,1212)
print(time3)

# The error occurs because the replace method is a method of datetime and time objects, not string objects
time4=time2.replace(hour=13,second=12)
print(time4)

Ftime=time2.strftime("%I:%M %p")
print(Ftime)

import time
current_time=time.time()
print(current_time)

''' print("starting...")
time.sleep(2)
print("finished...") '''

seconds=7200
hours=seconds//3600
minutes=(seconds%3600)//60
seconds=seconds%60
print(hours,minutes,seconds)

start_time=time.process_time()
end_time=time.process_time()
cpu_time=end_time-start_time
print(cpu_time)