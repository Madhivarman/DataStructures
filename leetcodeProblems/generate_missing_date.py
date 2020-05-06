import pandas as pd
import numpy as np
from calendar import monthrange

def monthly_wise_last_date(y, mm):
        if mm == 2:
            m = '{}-0{}-{}'.format(y, mm, 28)
        elif mm%2 !=0 or mm==8:
            #missing date value
            if mm < 10:
                m = '{}-0{}-{}'.format(y, mm, 31)
            else:
                m = '{}-{}-{}'.format(y, mm, 31)
        else:
            if mm < 10:
                m = '{}-0{}-{}'.format(y, mm, 30)
            else:
                m = '{}-{}-{}'.format(y, mm, 30)
        
        return m

def fill_missing_dates(sd, ed):
    missing_dates = []
    sy, ey = sd.year, ed.year  #start year, end year
    sm, em = sd.month, ed.month #start month, end month

    cy, cm = sy, sm #current  year, current month

    #loop through the dates
    while((cy <= ey and cm <= em) or (cy <= ey and cm >= em)):
        
        #once it reach the end date, return the values
        if((cm == em) and (cy == ey)):
            return missing_dates

        #check if the next dates is possible
        if(cm < 12):
            date = monthrange(cy, cm)[1] #gives the day
            dates = '{}-{}-{}'.format(cy,cm, date)
            #dates = monthly_wise_last_date(cy, cm)
            #dates = monthly_wise_last_date(cy, cm)
            missing_dates.append(dates)
            cm += 1

        elif(cm == 12):
            date = monthrange(cy, cm)[1] #gives the day
            dates = '{}-{}-{}'.format(cy,cm, date)
            #dates = monthly_wise_last_date(cy, cm)
            missing_dates.append(dates)
            cy += 1
            cm = 1 #update the month

        else:
            cm = 1 #update the current month
            cy += 1 #update the current year
    
    return missing_dates

start_date = pd.to_datetime('2018-11-30')
end_date = pd.to_datetime('2020-12-31')

tc2_sd = pd.to_datetime('2018-11-30')
tc2_ed = pd.to_datetime('2019-05-31')

tc3_sd = pd.to_datetime('2018-11-30')
tc3_ed = pd.to_datetime('2019-04-30')

tc4_sd = pd.to_datetime('2018-01-31')
tc4_ed = pd.to_datetime('2018-06-30')

tc5_sd = pd.to_datetime('2019-01-31')
tc5_ed = pd.to_datetime('2019-07-31')

tc1 = [start_date, end_date]
tc2 = [tc2_sd, tc2_ed]
tc3 = [tc3_sd, tc3_ed]
tc4 = [tc4_sd, tc4_ed]
tc5 = [tc5_sd, tc5_ed]

print(fill_missing_dates(tc1[0], tc1[1]))
print("-" * 15)
print(fill_missing_dates(tc2[0], tc2[1]))
print("-" * 15)
print(fill_missing_dates(tc3[0], tc3[1]))
print("-" * 15)
print(fill_missing_dates(tc4[0], tc4[1]))
print("-" * 15)
print(fill_missing_dates(tc5[0], tc5[1]))
print("-" * 15)

