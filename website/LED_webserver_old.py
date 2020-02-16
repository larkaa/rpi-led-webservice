#!/usr/bin/python3

import os
import sys
#print(sys.path)
from flask import Flask, request, redirect, url_for, render_template, flash, render_template_string
from werkzeug.utils import secure_filename
import generate_photo
import subprocess
import psutil
import time
import random


UPLOAD_FOLDER = './uploads'
PREVIEW_FOLDER = './preview'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
#app = Flask(__name__, debug=True)
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'





def allowed_file(filename):
    return('.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)



@app.errorhandler(404)
def page_not_found(e):
    flash("Page not found.") 
    return(redirect(url_for('upload_file')))
    
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    light=1.0
    color = "51,119,255"
    rand = False
    
    if request.method == 'POST':

        for i in request.form:
            print(i,request.form[i])
            if 'random' in i:
                rand = True
                
        if rand:
            rand = random.choice(os.listdir('/home/pi/Desktop/gifs/'))
            #print(rand)       
            proc_s = 'sudo /home/pi/code/rpi-rgb-led-matrix/utils/led-image-viewer --led-cols=64 --led-rows=32 --led-brightness=50 -t7 -C /home/pi/Desktop/gifs/{}'.format(rand)
            print(proc_s)
            
        else:
            light = request.form["brightness"] 
            light = int(light)
            color = request.form["text_color"].replace(' ','').strip()
            print(color)
            cap = request.form["caption"]
            proc_string1 = 'sudo /home/pi/code/rpi-rgb-led-matrix/examples-api-use/demo --led-cols=64 --led-rows=32 -D11 -t 2.2'
            
            proc_string2 = 'sudo /home/pi/code/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-cols=64 --led-rows=32 -s 8 -b {} -f fonts/7x13B.bdf -C {} -y 8 -l 3 "{}"'.format(light, color, cap)
            
            #print(proc_string2) 
            proc_s = proc_string1+';'+proc_string2
            print(proc_s)
            

        #flash("Showing: "+ cap)
        f = True
        ### make sure the process is not curretnly running
        while f:
            f = False
            for q in psutil.process_iter():
                #print(q.name(),q.cmdline())
                if q.name():
                    temp = q.cmdline()
                    if 'led-image-viewer' in q.name() or 'examples-api-use/demo' in temp or 'examples-api-use/scrolling-text-example' in temp:
                        #print(temp)
                        f=True
            time.sleep(.1)
        
        
        try:
            #subprocess.run(['sudo',proc_string1],shell=True)
            subprocess.run(proc_s,shell=True)
            #subprocess.run(proc_string2,shell=True)
            
        except Exception as e:
            flash('Oops, try again')
            print(e)
        
        
        #print(proc_string)
        # check if the post request has the file part
        '''
        if 'file' not in request.files:
            flash('No file part')
            return(redirect(request.url))
        
        file = request.files['file']
        print(cap)
        print(light, request.files['file'])
        print()
        
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return(redirect(request.url))
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            randfilename = generate_photo.update_img(os.path.join(app.config['UPLOAD_FOLDER'], filename), cap,light)

            return(redirect(url_for("preview_file",filename = randfilename)))
    '''
    return(render_template('index.html'))
    
@app.route('/waterplant',methods=['GET'])
def water_plant():
    plant_no = request.args['id']
    print('\nid=',plant_no)
    
    if plant_no == 1:
        filename = 'plant1_a.jpg'
        show_img(filename)
    elif plant_no == 2:
        filename = 'plant2_a.jpg'
        show_img(filename)
    else:
        pass

    return(temp)
    
    

'''

@app.route('/preview/<filename>', methods=['GET','POST'])
def preview_file(filename):
    print(os.path.join('uploads', filename))
    
       
    filename1 = filename + 'a.jpg'
    filename2 = filename + 'b.jpg'
    filename3 = filename + 'c.jpg'
    filename4 = filename + 'd.jpg'
    filename5 = filename + 'e.jpg'
    
    exists = os.path.isfile(os.path.join('static', filename1))
    if not exists:
        flash("File or page does not exist. Start over.")
        return(redirect(url_for('upload_file')))
     
        

    
    if request.method == 'POST':
        target = request.form.get('img_type')

            
        if request.form['submit_button'] == 'Publish Photo':
            
            if target == 'im_1':
                
                generate_photo.show_img('./static/'+filename1)
            elif target == 'im_2':
                
                generate_photo.show_img('./static/'+filename2)
            elif target == 'im_3':
                
                generate_photo.show_img('./static/'+filename3)
            elif target == 'im_4':
                
                generate_photo.show_img('./static/'+filename4)
            elif target == 'im_5':
                
                generate_photo.show_img('./static/'+filename5)
            else:
                print('error')
                
            os.remove('./static/'+filename1)
            os.remove('./static/'+filename2)
            os.remove('./static/'+filename3)
            os.remove('./static/'+filename4)
            os.remove('./static/'+filename5)
        
            #return(render_template('index.html'))
            return(redirect(url_for('upload_file')))
   
        
        elif request.form['submit_button'] == 'Start Over':
            #print('Going back')
            os.remove('./static/'+filename1)
            os.remove('./static/'+filename2)
            os.remove('./static/'+filename3)
            os.remove('./static/'+filename4)
            os.remove('./static/'+filename5)
            return(redirect(url_for('upload_file')))
        
        elif request.method == 'GET':
            return(render_template('preview.html',
                                   user_img1 = '/static/'+filename1,
                                   user_img2 = '/static/'+filename2,
                                   user_img3 = '/static/'+filename3,
                                   user_img4 = '/static/'+filename4,
                                   user_img5 = '/static/'+filename5))
        
        
    return(render_template('preview.html',
                                user_img1 = '/static/'+filename1,
                                user_img2 = '/static/'+filename2,
                                user_img3 = '/static/'+filename3,
                                user_img4 = '/static/'+filename4,
                                user_img5 = '/static/'+filename5))
'''



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True, threaded=True)
