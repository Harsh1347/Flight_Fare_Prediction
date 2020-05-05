import pandas as pd
import numpy as np
import requests
import json
import time
from pandas.io.json import json_normalize
from datetime import timedelta
from datetime import datetime

search_date = datetime.today().date()
source = "DEL"
print("started")
for city in [0,1,2,3]:
    if city == 0:
        destination = "BOM"
    elif city ==1:
        destination = "HYD"
    elif city == 2:
        destination = "PNQ"
    else:
        destination = "NAG"
    details = []
    #print(destination)
    for t in range(93):
        if(t%29 == 0): #Restriction of api(only 30 calls a min)
            time.sleep(60)

        dep_date = datetime.today()+ timedelta(t)
        dep_date = dep_date.date()
        days2fly = str(dep_date - search_date).split()[0]
        if(days2fly == '0:00:00'):
            days2fly = 0
        else:
            days2fly = int(days2fly)
        #print(search_date,dep_date)
        Depdate = int("".join(str(dep_date).split('-')))
        
        url ="http://developer.goibibo.com/api/search/?app_id=<your_id>&app_key=<your_key>&format=json&source={}&destination={}&dateofdeparture={}&seatingclass=E&adults=1&children=0&infants=0&counter=100".format(source,destination,Depdate)
        results = (requests.get(url).json()['data']['onwardflights'])
        

        for i in range(len(results)):
            #print(len(results),i,dep_date,destination)
            ri = results[i]
            #print(ri['deptime'])
            if(int(ri['stops']) == 2):
                if(str(ri['onwardflights'][1]['destination']) == destination):

                
                    try:#print((ri['onwardflights'][1]),ri['stops'])
                        details.append((search_date,dep_date,days2fly, ri['origin'],ri['onwardflight'][1]['destination'],
                        ri['deptime'],ri['onwardflights'][1]['arrtime'],
                        ri['flightno'],ri['airline'],ri['fare']['totalfare'],ri['seatsavailable'],
                        ri['seatingclass'],ri['duration'],ri['stops'],
                        ri['onwardflights'][0]['origin'],
                        ri['onwardflights'][1]['origin']))
                        
                    except:
                        details.append((search_date,dep_date,days2fly,ri['origin'],ri['onwardflights'][1]['destination'],
                        ri['deptime'],ri['onwardflights'][1]['arrtime'],
                        ri['flightno'],ri['airline'],ri['fare']['totalfare'],ri['seatsavailable'],
                        ri['seatingclass'],ri['duration'],ri['stops'],
                        ri['onwardflights'][0]['origin'],
                        ri['onwardflights'][1]['origin']))
                        

            if(int(ri['stops']) == 1):
                if(str(ri['onwardflights'][0]['destination']) == destination):
                
                    details.append((search_date,dep_date,days2fly,ri['origin'],ri['onwardflights'][0]['destination'],
                    ri['deptime'],ri['onwardflights'][0]['arrtime'],
                    ri['flightno'],ri['airline'],ri['fare']['totalfare'],ri['seatsavailable'],
                    ri['seatingclass'],ri['duration'],ri['stops'],
                    ri['onwardflights'][0]['origin'],'NA'))
            else:
                if(str(ri['destination']) == destination):
                    details.append((search_date,dep_date,days2fly,ri['origin'],ri['destination'],
                    ri['deptime'],ri['arrtime'],
                    ri['flightno'],ri['airline'],ri['fare']['totalfare'],ri['seatsavailable'],
                    ri['seatingclass'],ri['duration'],ri['stops'],
                    'NA','NA'))
                
    #print(details)
    finalData = pd.DataFrame(details)
    finalData.columns = ['Search_Date','Departure_Date','Days_fly','origin','destination',
        'deptime','arrtime',
        'flightno','airline','Total_fare','seats_avail',
        'seatingclass','duration','stops',
        'stop1','stop2']
    finalData.drop_duplicates(inplace = True)
    #finalData.to_csv('<location>'+'RawFlight.csv',mode = 'a',header = True)
    finalData.to_csv('<location>'+'RawFlight.csv',mode = 'a',header = False)
print(finalData,"!!!!<<<<done check file>>>>!!!!")


