import time
import pandas as pd
import numpy as np
from IPython.display import display

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True :
        city = input('Would you like to choose chicago,new york city or washington \n').lower()
        if city not in ['chicago','new york city','washington']:
            print('Please enter a correct city as shown')
        else: 
            break

    months = ['january','febraury','march','april','may','june','all']
    while True :
        month = input('Would you like to filter by a January,Febraury,March,April,May,June or All \n').lower()
        if month not in months:
            print('-'*40)
            print('Please enter a correct month or choose all')
            print('-'*40)
        else:
            break

    days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All']
    while True :
        day = input('Would you like to filter by Saturday,Sunday,Monday,........or All \n').lower().title()
        if day not in days:
            print('-'*40)
            print('Please enter a correct day or choose all')
            print('-'*40)
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    months_2 = ['january','febraury','march','april','may','june']
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        month = months_2.index(month)+1
        df = df[df['month'] == month]

    if day != 'All':
        df= df[df['day']== day]
        
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('-'*40)
    if month != 'all':
        print('You filtered by {}'.format(month.title()))
    else:
        months_2 = ['january','febraury','march','april','may','june']
        month_res = months_2[df['month'].mode()[0] - 1]
        print('Most Common month is : ' + month_res.title() )
        
    if day !='All':
        print('You filtered by {}'.format(day))
    else:
        day_res = df['day'].mode()[0]
        print('Most Common day is : ' + day_res)
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    hour_res = df['hour'].mode()[0]
    if hour_res >12:
        print('Most Common hour is : ' + str(hour_res-12) + ' pm' )
    else:
        print('Most Common hour is : ' + str(hour_res) + ' am')
    print('-'*40)
    return 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('-'*40)
    most_start = df['Start Station'].mode()[0]
    print('Most Common Start Station : ' + most_start)
    print('-'*40)
    most_end = df['End Station'].mode()[0]
    print('Most Common End Station : ' + most_end)
    print('-'*40)
    df['Trip SE'] = df['Start Station'] +' to ' +df['End Station']
    most_trip = df['Trip SE'].mode()[0]
    print('Most Common Trip : From ' + most_trip)
    return


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('-'*40)
    total_travel = df['Trip Duration'].sum().round()
    print('Total Travel time is : ' + str(total_travel) )
    avg_travel = float(round(df['Trip Duration'].mean()))
    print('Average Travel time is : ' + str(avg_travel) )
    return

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('-'*40)
    user_type_counts = df['User Type'].value_counts()
    print('Number of Subscribers is : ' + str(user_type_counts['Subscriber']))
    print('Number of Customers is : ' + str(user_type_counts['Customer']))
    
    if city !='washington':
        print('-'*40)
        gender_counts = df['Gender'].value_counts()
        print('Number of Males is : ' + str(gender_counts['Male']))
        print('Number of Females is : ' + str(gender_counts['Female']))
        print('-'*40)
        earliest_year = df['Birth Year'].min()
        mostrecent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth is : ' + str(earliest_year))
        print('Most recent year of birth is : ' + str(mostrecent_year))
        print('Most common year of birth is : ' + str(most_common_year))
    return


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_five(df):
    rows= 0
    while True:
        print('-'*40)
        x = input('Would you like to show 5 lines of the data (Yes or No) \n').lower()
        if x == 'yes':
            past_rows = rows
            rows += 5
            if city !='washington':
                result = df.iloc[past_rows:rows,0:9]
            else:
                result = df.iloc[past_rows:rows,0:7]
            display(result)
        elif x == 'no':
            break
        else:
            print('-'*40)
            print('Please enter Yes or No')
    return


def main():
    while True:
        global city,month,day
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_five(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
