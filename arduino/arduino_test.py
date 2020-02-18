#!/usr/bin/env python3
# Import de la librairie serial
import serial
import time

# Ouverture du port serie avec :
# '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
# 9600 : vitesse de communication
ser = serial.Serial('/dev/ttyUSB0', 9600)


# Ecriture de chaque message recu
#ser.write(b'5')
#ser.write(b'0')
#time.sleep(.3)
count=0
while True:
    #print(ser.readline())
    ser.write(b'1')
    
    #count+=1
    temp = int(ser.readline().strip())
    if temp==1:
        break
    count+=1
time.sleep(4)
ser.write(b'2')
time.sleep(4)
ser.write(b'3')

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
