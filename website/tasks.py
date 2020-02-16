import psutil
import subprocess
import time

def push_to_led(process_string):
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
        subprocess.run(process_string,shell=True)
    except Exception as e:
        #flash('Oops, try again')
        print(e)
    return
            

        