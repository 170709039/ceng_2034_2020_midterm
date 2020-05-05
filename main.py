import os
from sys import platform
import multiprocessing


print('MIDTERM 2034 - Student: Mustafa Şükrü Kapusuz - 170709039');

# Assigment 1
## Print PID of itself
print('Current process id:' + str(os.getpid()))

# Assigment 2
## If the running OS is linux; print loadavg.
if(platform=='Linux'):
    print("Linux Load Avarages:" + str(os.getloadavg()))


# Assigment 3
## Take and print “5 min loadavg” value and cpu core count. If the loadavg value is near
## (or close) to the cpu core count (hint: nproc - 5min loadavg < 1) then exit script.
load_avg1, load_avg5, load_avg15 = os.getloadavg()

# take CPU count
cpu_count = multiprocessing.cpu_count()

# If the loadavg values is near to CPU core count then exit script.
if( (cpu_count - load_avg5) < 1 ):
    exit()

