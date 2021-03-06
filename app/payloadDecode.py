from datetime import datetime
from logging import lastResort
from pytz import timezone

def getDate():
    nai = timezone('Africa/Nairobi')
    now_date=datetime.now().astimezone(nai)
    d= now_date.strftime("%m/%d/%y, %H:%M")
    return d


def locationPin (testString):
    polarityHex=testString[2:4]
    polarityInt=int(polarityHex, base=16)
    if (polarityInt==0):
        latitudePosition='-'
        longitudePosition='-'
    elif(polarityInt==1):
        latitudePosition="-"
        longitudePosition="+"
    elif(polarityInt==10):
        latitudePosition="+"
        longitudePosition="-"
    elif(polarityInt==11):
        latitudePosition="+"
        longitudePosition="+"
    else:
        print("Polarity not defined")
  

    # getting the latitude

    latitudeHex=testString[4:12]
    latitudeInt=int(latitudeHex,base=16)
    latitudeOriginal=float(latitudeInt/10000000)
    lat=latitudePosition+str(latitudeOriginal)

    #getting the longitude
    longitudeHex=testString[12:20]
    longitudeInt=int(longitudeHex,base=16)
    longitudeOriginal=float(longitudeInt/10000000)
    long=longitudePosition+str(longitudeOriginal) 

    return lat, long

def battery (testString):

    N=2
    length= len(testString)

    batteryhex=testString[length - N: ]
    batteryInt=int(batteryhex, base=16)
    return batteryInt

def level (testString):
    levelhex=testString[2:6]
    levelInt=int(levelhex, base=16)
    return levelInt


def surveyDecode( testString):
    #check if tampered with
    tampered=testString[ :2]
    tamperedInt=int(tampered, base=16)
    if (tamperedInt==31):
        tamperedBool=True
    elif (tamperedInt==15):
        tamperedBool=False
    #get the location also
    latSurvey, longSurvey=locationPin(testString)

    return tamperedBool, latSurvey, longSurvey