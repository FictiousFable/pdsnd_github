import time
import pandas as pdi
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Month_Data = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

Day_Data = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\n Please input what city you would like to review: \n")
        if city_name.lower() in CITY_DATA:
            city = city_name
        else:
            print("That is not a valid city option. Please select either Chicago, New York City, or Washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in Month_Data:
        month_name = input("\n What is the month you would like to view?: \n")
        if month_name.lower() in Month_Data:
            month = month_name
        else:
            print("That is not a valid month option. Please enter month from January to June, or all.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ''
    while day_of_week.lower() not in Day_Data:
        day_of_week = input("\n What is the day of the week you would like to view?:\n")
        if day_of_week.lower() in Day_Data:
            day = day_of_week
        else:
            print("That is no a vaild day option. Please enter any day of the week, or all:\n")

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
    
    
    df = pdi
.read_csv(CITY_DATA[city.lower()])
    
    df['Start Time'] = pdi
.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    
    if month != 'all':
        df = df[df['month'].str.startswith(month.title())]
    
    if day != 'all':
        df = df[df['day_of_week'].str.startswith(day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print('The most common month for travel is: ', common_month)
    
    # TO DO: display the most common day of week
    
    common_day = df['day_of_week'].mode()[0]
    print('The most common day for travel is: ', common_day)

    # TO DO: display the most common start hour
    
    common_hour = df['hour'].mode()[0]
    print('The most common hour for travel is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most common start station is: \n', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common end sation is: \n', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    
    station_combination = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('The most common station combination is: \n {}'.format(station_combination))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time    
    travel_time = round(df['Trip Duration'].sum())
    minute, second = divmod(travel_time, 60)
    hour, minute = divmod(minute, 60)
    
    print('The total travel time is {} hours, {} minutes, and {} seconds.'.format(hour,minute,second))

    # TO DO: display mean travel time
    average_time = round(df['Trip Duration'].mean())
    minute, second = divmod(average_time, 60)
    hour, minute = divmod(minute, 60)
    print('The average travel time is {} hours, {} minutes, and {} seconds'.format(hour,minute,second))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count for differnt User Types is:', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    
    try:
        print('The count for genders is:', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest birth year is: ', df['Birth Year'].min())
                         
        print('The most recent birth year is: ', df['Birth Year'].max())
                             
        print('The most common birth year is: ', df['Birth Year'].mode()[0])
    
    except:
        print('There is no filter for Gender or Birth Year in Washington City.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def ask_display(df):
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no: \n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
