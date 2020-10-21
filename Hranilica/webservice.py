from flask import Flask, request
from flask_cors import CORS
import RPi.GPIO as GPIO
import json
import _thread
import time
import datetime
import testsenzor as ts
import motorscript as ms

app = Flask(__name__)
CORS(app)

hour = 1
minute = 1
portionSize = -1
ms.portionDistance = 15



@app.route('/')
def index():
    return json.dumps({'poruka':"Cao"})

@app.route('/dajbroj', methods=['GET'])
def dajBroj():

    hours = request.args.get('hour')
    minutes = request.args.get('minute')
    global hour
    hour = hours
    global minute
    minute = minutes
    
    return "ok"

@app.route('/dajporciju', methods=['GET'])
def dajPorciju():

    size = request.args.get("size")
    global portionSize
    portionSize = size
    
    return "ok2"
    
#nova ruta za sipanje odmah
@app.route('/sipajodmah', methods=['GET'])
def sipanje():
    ms.sipaj()
    return "ok"



def proveraVremena():
    
    while True:
        
        timee = datetime.datetime.now()
        print(timee)
        print(timee.hour)
        print(timee.minute)
        
        if timee.hour == int(hour) and timee.minute == int(minute):
            #sipanje
            ms.sipaj()
        time.sleep(61)
        


_thread.start_new_thread(proveraVremena, ())


if __name__=="__main__":
    try:
        time.sleep(2)
        app.run(host = "0.0.0.0")
    except KeyboardInterrupt:
        GPIO.cleanup()
