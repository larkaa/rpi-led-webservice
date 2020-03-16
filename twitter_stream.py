#!/usr/bin/env python3
import tweepy  
import re
from redis import Redis
from rq import Queue
import sys
sys.path.insert(1,'/home/pi/code/rpi-led-webservice/website')
from tasks import push_to_led,play_sound
# Consumer keys and access tokens, used for OAuth
from twitter_auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    follow_id
)


# Redis queue
q = Queue(connection=Redis())



# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
  
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)  

class LEDStreamer(tweepy.StreamListener):
    def on_status(self, status):
        #print(status.user.screen_name)
        #print(status.entities['hashtags'])
        #print()
        sound=False
        try:
            temp = status.extended_tweet['full_text']
        except:
            temp = status.text
        text = "{}: {}".format(status.user.name.split(' ')[0],
                               temp)
        text = status.text
        text = text.replace('@132Vert','').strip()
        #pattern = re.compile('#\S*')
        #text = pattern.sub('',text).strip()
        
        if '#z' in temp.lower():
            sound = 1
            play_sound(num=sound)
            text = text.replace('#z','').strip()
        if '#beep' in temp.lower():
            sound = 2
            play_sound(num=sound)
            text = text.replace('#beep','').strip()
        if '#bell' in temp.lower():
            sound = 3
            play_sound(num=sound)
            return
        
        proc_string1 = 'sudo /home/pi/code/rpi-led-webservice/utils/led-image-viewer --led-cols=64 --led-rows=32 --led-brightness=75 -C -w1 /home/pi/code/rpi-led-webservice/twitter.png /home/pi/code/rpi-led-webservice/twitter.png'
        proc_string2 = 'sudo /home/pi/code/rpi-led-webservice/examples-api-use/scrolling-text-example --led-cols=64 --led-rows=32 -s 8 -b {} -f /home/pi/code/rpi-led-webservice/fonts/7x13B.bdf -C {} -y 8 -l 3 "{}"'.format('75', '29,161,242', text)

        proc_s = proc_string1+';'+proc_string2
        
        q.enqueue(push_to_led, proc_s, result_ttl=0)
        print(text)

led_listener = LEDStreamer()
print('starting stream...')
mystream = tweepy.Stream(auth = api.auth, listener=LEDStreamer())

#mystream.filter(follow=[follow_id])
mystream.filter(track=["132Vert"])


