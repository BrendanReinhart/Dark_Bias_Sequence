#!/usr/bin/env python
import sys, os, commands, math, string
from os import path
#os.system('cp -f ~/login.cl .'); from pyraf import *

import numpy as np
import time
import subprocess
#import pyfits as pf
#import matplotlib.pyplot as plt
from termcolor import colored
#if __name__ == '__main__':


#make sure you run    camera_monitor --echo   in terminal before executing this script!

#DEFINE PARAMETERS HERE
port = 7078                 #port number of CCD
exp = 600                   #exposure time for Darks, in seconds
numd = 15                   #number of darks
numb = 10                   #number of biases
rest = 30                   #rest time between darks in seconds. Recommended min = 10

#subprocess line for camera temp regulation. Waits a minute for temp to drop.
subprocess.check_output('send localhost 7078 "regulate -5"', shell=True)
time.sleep(300)

#print 'Welcome Huntsman! Beginning 10x 600s dark sequence.'
print('Welcome Huntsman! Beginning ' +str(numd)+'x ' + str(exp)+'s dark sequence.')
#command = 'send localhost 7078 "expose dark 600"'
command = 'send localhost 7078 "expose dark 600"'
commandb = 'send localhost 7078 "expose bias 0.1"'
#command = 'send localhost ' + str(port) + ' "expose dark ' + str(exp) +'"'

for n in range(1,numd+1):
    print('Commencing dark #' + str(n))
    subprocess.check_output(command, shell=True)
    time.sleep(exp+rest)
    #if statement below to tackle the last iteration not printing commencing next.
    print('Dark #' + str(n) + ' complete.')
    n=n+1
print 'Dark sequence complete!'    

print('Beginning ' +str(numb)+'x bias sequence.')        
for n in range(1,numb+1):
    print('Commencing bias #' + str(n))
    subprocess.check_output(commandb, shell=True)
    time.sleep(10)
    print('bias #' + str(n) + ' complete.')
    #if statement below to tackle the last iteration not printing commencing next.
    #print('bias #' + str(n) + ' complete. Commencing bias #' + str(n+1))
    n=n+1
        
    
print 'Bias sequence complete!'
print 'All images complete.'

subprocess.check_output('send localhost 7078 "deregulate"', shell=True)

#add subprocess line for camera temp deregulation.



    
#command = 'send localhost 7078 "expose dark 600"'

#print 'Commencing dark #1..'
#subprocess.check_output(command, shell=True)
#time.sleep(610)
#print 'dark #1 complete. Commencing dark #2..'

#subprocess.check_output(command, shell=True)
#time.sleep(610)
#print 'dark #2 complete. Commencing dark #3..'

#subprocess.check_output(command, shell=True)
#time.sleep(610)
#print 'dark #3 complete.'

#print 'dark sequence complete!'