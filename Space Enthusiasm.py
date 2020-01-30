# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:34:36 2019

@author: alvar
"""
import requests

user_data = 0

# TRY CATH BLOCK IN EVERY JSON STUUFFFFFF!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# get user data and save for further processing
# https://randomuser.me/api/?inc=gender,name,location,nat
def userLogin(test=False):
    url = "https://randomuser.me/api/?inc=gender,name,location,nat"
    #Before going on, we check if status is 200, and if we can convert it to python object
    try:        
        user = requests.get(url)
        if not user.status_code == 200:
            print("HTTP error", user.status_code)
        else:
            try:
                user_data = user.json()
            except:
                print("User not in valid JSON format")
    except:
        print("Something went wrong with request.get")
        

    return user_data

#userLogin()

# define message template and fill with data for the user
# display using print(...)

def displayMessage():
    #We don't want the global variable to have always the same values
    global user_data
    user_data = userLogin()
    #print(user_data)
    
    #Recollect the values of every function to the print statement
    try:
        user_name = getUserName()
        user_coordinates = getUserCoordinates()
        user_city = getUserCity()
        iss_coordinates = getIssCoordinates()
        iss_passtime = getIssPassTime(user_coordinates)
        time = convert(iss_passtime)
        people_space = getPeopleInSpace()
        distance = getDistance(user_coordinates, iss_coordinates)
    except Exception as error:
        return error

    
    print(f"Welcome {user_name['title']}. {user_name['first']} {user_name['last']}. You are now {distance} km away from ISS.")
    print(f"No worries, ISS will pass by your location in {user_city} on {time}.")
    print(f"Currently, there are {people_space} people in space.")
    
# title, first, last
def getUserName():
    user =  user_data['results'][0]
    #print(user['location']['country'])
    
    title = user['name']['title']
    first = user['name']['first']
    last = user['name']['last']
    
    name = {'title' : title, 'first': first, 'last' : last}
        
    return (name)
    
# where is the user located?
def getUserCoordinates():
    user_coordinates = {'latitude': user_data['results'][0]['location']['coordinates']['latitude'], 
                   'longitude': user_data['results'][0]['location']['coordinates']['longitude']}
    
    return user_coordinates
    
# in which city does the user live?    
def getUserCity():
    city = user_data['results'][0]['location']['city']
    
    return city
    
# fetch ISS position through web api
# http://api.open-notify.org/iss-now.json   
def getIssCoordinates(test=False):
    url = "http://api.open-notify.org/iss-now.json"
    iss = requests.get(url).json()
    iss_coordinates = {'longitude': iss['iss_position']['longitude'],
                      'latitude':iss['iss_position']['latitude']}
    
    return iss_coordinates

# fetch ISS pass timestamp for given coordinates
# modify URL as required
# http://api.open-notify.org/iss-pass.json?lat=45.0&lon=-122.3
def getIssPassTime (userCoord, test=False):
    user_lat =userCoord['latitude']
    user_lon = userCoord['longitude']
    try:
        
        url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(user_lat) + '&lon=' + str(user_lon)
        iss_time = requests.get(url).json()
        #print(iss_time)
        
        iss_time = {'duration': iss_time['response'][0]['duration'], 
                    'risetime': iss_time['response'][0]['risetime']}
        #print(iss_time)
        
    except Exception:
        print("Oops, something went wrong while obtaining the JSON data from the server, please try again")
        
    else:
        return iss_time

# convert unix timestamp to date in users' timezone
def convert(timestamp):
    
    import datetime
    import pytz
    
    time = timestamp['risetime']
    #lala = datetime.datetime.utcfromtimestamp(time).replace(tzinfo=datetime.timezone.utc)
    #print("printing lala",lala)
    #print(time)
    #time_ = datetime.datetime.fromtimestamp(time)
    #print("before utc: ",type(time_), time_,)
    time = datetime.datetime.fromtimestamp(time, pytz.utc)
    #print("after utc (00): ",type(time), time,)
     
    #We get the user UTC
    utc_user = user_data['results'][0]['location']['timezone']['offset']    
    #print("\n trying to see the user utc",type(utc_user), utc_user)
    
    #We get the hours, minutes of that UTC
    utc_user_separate = utc_user.split(":")
    #print("utc_user_separate : ", utc_user_separate)   
    utc_user_hours, utc_user_minutes = utc_user_separate[0],utc_user_separate[1]
    
    #We add the difference to our UTC 00 date
    time_utc= time + datetime.timedelta(hours=int(utc_user_hours))
    time_utc = time_utc + datetime.timedelta(minutes = int(utc_user_minutes))
    #print(time_utc)
    
    # We give the format to the date required.
    formato = "%b %d, %Y at %H:%M:%S"
    time_utc = datetime.datetime.strftime(time_utc,formato)
    #print(type(time_utc), time_utc)

    return time_utc

#convert(getIssPassTime(getIssCoordinates()))
    
# fetch data about people in space
# http://api.open-notify.org/astros.json
def getPeopleInSpace(test=False):
    url = "http://api.open-notify.org/astros.json"
    people = requests.get(url).json()
    people_number = people['number']
    
    return people_number
    
    
#getPeopleInSpace()

# calculate distance between two geo locations
def getDistance(userCoord, issCoord):
    from math import sin, cos, sqrt, atan2, radians
    #import geopy.distance
   
    #user_pos = (float(userCoord['latitude']), float(userCoord['longitude']))
    #iss_pos = (float(issCoord['latitude']), float(issCoord['longitude']))
    
    #distancia = round(geopy.distance.geodesic(user_pos,iss_pos).km)
    #print(distancia)
    
    #Radius Earth
    R = 6378
    
    lat1=radians(float(userCoord['latitude']))
    lat2=radians(float(issCoord['latitude']))
    dlat=lat2-lat1
    
    lon1=radians(float(userCoord['longitude']))
    lon2=radians(float(issCoord['longitude']))
    dlon=lon2-lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = (R*c)
    distance = round(distance)
    
    return distance
    

displayMessage()    