import psutil
import subprocess
import time
import serial

def play_sound(num=1):
    
    with serial.Serial('/dev/ttyUSB0', 9600,timeout=1) as ser:
    
    #try:
    #    ser = serial.Serial('/dev/ttyUSB0', 9600)
    #except:
    #    ser = serial.Serial('/dev/ttyUSB1', 9600)
        
    #time.sleep(.01)
    
        if num == 1:
            while True:
                ser.write(b'1')
                ser.flush()
                temp = int(ser.readline().strip())
                if temp==num:
                    ser.close()
                    return
                time.sleep(.1)
                
        elif num == 2:
            while True:
                ser.write(b'2')
                ser.flush()
                temp = int(ser.readline().strip())
                if temp==num:
                    ser.close()
                    return
                time.sleep(.1)
                
        elif num == 3:
            while True:
                ser.write(b'3')
                ser.flush()
                temp = int(ser.readline().strip())
                if temp==num:
                    ser.close()
                    return
                time.sleep(.1)
        else:
            ser.close()
            return
    

def push_to_led(process_string, sound = 0):
    start = time.time()
    f = True
    ### make sure the process is not currently running
    while f:
        f = False
        for q in psutil.process_iter():
            #print(q.name(),q.cmdline())
            if q.name():
                temp = q.cmdline()
                if 'led-image-viewer' in q.name():
                    f=True
                if ('examples-api-use/demo' in temp):
                    f = True
                if ('examples-api-use/scrolling-text-example' in temp):
                    f=True
                if f==True and time.time() - start > 30:
                    return
                if f==True:
                    time.sleep(.5)
    
    try:
        #print(process_string)
        #p1,p2 = process_string.split(';')
        #print(p2)
        if sound:
            play_sound(1)
        subprocess.run(process_string,shell=True)
    except Exception as e:
        #flash('Oops, try again')
        print(e)
    return
            

        