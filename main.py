import os
from sys import platform
import multiprocessing
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

print('MIDTERM 2034 - Student: Mustafa Şükrü Kapusuz - 170709039');

# Assigment 1

print('Assigment 1')

## Print PID of itself
print('Current process id:' + str(os.getpid()))




# Assigment 2

print('\n')
print('Assigment 2')

## If the running OS is linux; print loadavg.
if(platform=='Linux'):
    print("Linux Load Avarages:" + str(os.getloadavg()))







# Assigment 3

print('\n')
print('Assigment 3')

## Take and print “5 min loadavg” value and cpu core count. If the loadavg value is near
## (or close) to the cpu core count (hint: nproc - 5min loadavg < 1) then exit script.
load_avg1, load_avg5, load_avg15 = os.getloadavg()

# take CPU count
cpu_count = multiprocessing.cpu_count()

# If the loadavg values is near to CPU core count then exit script.
if( (cpu_count - load_avg5) < 1 ):
    exit()







#Assigment 4

print('\n')
print('Assigment 4')

URLs = [

    'https://api.github.com',
    'http://bilgisayar.mu.edu.tr/',
    'https://www.python.org/',
    'http://akrepnalan.com/ceng2034',
    'https://github.com/caesarsalad/wow'

]


def check_status(url):
    req = requests.get(url, stream=True)

    if req.status_code>=200 and req.status_code<300:
        status = 'Success, Working'
    elif req.status_code>=400 and req.status_code<600:
        status = 'Failed, Not Working'


    return url + ' : ' + status

processes = []

with ThreadPoolExecutor(max_workers=5) as executor:
    for url in URLs:
        processes.append(executor.submit(check_status, url))

for task in as_completed(processes):
    print(task.result())