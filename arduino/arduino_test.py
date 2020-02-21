#!/usr/bin/env python3
# Import de la librairie serial
import serial
import time

# Ouverture du port serie avec :
# '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
# 9600 : vitesse de communication
#ser = serial.Serial('/dev/ttyUSB0', 9600)
#time.sleep(.05)
#print('sleep')


with serial.Serial('/dev/ttyUSB0', 9600,timeout=1) as ser:
    ser.write(b'1')
    ser.flush()
    temp = ser.readline()
    print(temp)
    temp = temp.strip()
    print('temp: ',temp)
    #time.sleep(4)

# Ecriture de chaque message recu
#ser.write(b'5')
#ser.write(b'0')
#time.sleep(.3)
#count=0
#while True:
    #print(ser.readline())
#ser.write(b'1')

#count+=1
#temp = ser.readline().strip()
#print(temp)
#if int(temp)==1:
#    break
#count+=1
#ser.close()
#time.sleep(4)
#ser.write(b'2')
#time.sleep(4)
#ser.write(b'3')

#    if int(temp)==2:
#        break
#    time.sleep(.1)
    

#print("Secret!")
#ser.write(b'2')
#ser.write(b'2')
#ser.write(b'2')
#time.sleep(5)
#print("Beep")
#ser.write(b'1')
#time.sleep(5)
#print(ser.readline())
