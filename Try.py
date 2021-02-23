import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True :
        try:
            city = input('Would you like to choose chicago,new york city or washington')
        if city not in ['chicago','new york city','washington']:
            except:
                print('Please enter a correct city')
        else:
            break 
return city
