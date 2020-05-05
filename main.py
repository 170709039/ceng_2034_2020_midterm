import os
from sys import platform


print('MIDTERM 2034 - Student: Mustafa Şükrü Kapusuz - 170709039');

# Assigment 1
## Print PID of itself
print('Current process id:' + str(os.getpid()))

# Assigment 2
## If the running OS is linux; print loadavg.
if(platform=='Linux'):
    print(os.getloadavg())
