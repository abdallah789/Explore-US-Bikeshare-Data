import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #create city list
    cities=['chicago','new york','washington']
    #user city input
    city = input("Plz Enter the City here: ").lower()  #City is Lowered  to be like as exist in th cities list
    # Use a while loop to handle invalid inputs
    while True:
        if city in cities:
            break
        else:
            city = input("invalid input plz try again:")

    # TO DO: get user input for month (all, january, february, ... , june)
    #Creating month list
    months = ['january','february','march','april','may','june','all']
    #user month input
    month = input("Please enter the month, between January to June:").lower().strip()
    #creating while loop to repeat the process till the user write the correct input 
    while True:
        if month in months:
            break
        else:
            month = input("invalid input plz try again:").lower().strip()    
    if month != 'all':
        print(f'the chosen month is {month}')
    else:
        print("all months are chosen")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Creating a day list
    days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    #user day input
    day = input("\nPlease enter the week day:").lower().strip()
    #creating while loop to repea the process till the user write the correct input 
    while True:
        if day in days:
            break
        else:
            day = input("\nInvalid input. Please try again.").lower().strip()
    if day != "all":
        print(f"\nthe selected day is {day}")
    else:
        print('all days are chosen')

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
    
    #load dataframe based on the chosen city
    df = pd.read_csv(CITY_DATA[city])
    #Convert the Start Time column(srting format) to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Now month and weekday can be extracted from start time column
    #create month column
    df['month'] = df['Start Time'].dt.month
    #cretae day_of_week column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #create another month list
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    #filter the data frame by month if the user dont chose 'all' option
    if month != 'all':
        df = df[df['month'] == months.index(month)+1]
    #Filter the data frame by the weekday if the user dont chose 'all' option
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)
    # TO DO: display the most common start hour
    #first create hour cloumn from from the "Start Time" column
    df['hour'] = df['Start Time'].dt.hour
    #then using value_counts().idxmax() to display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
        
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print(f"The most commonly used start station: {common_start_station}")
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print(f"The most commonly used start station: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    # Using + operator to combine two columns
    df['Start To End'] = df['Start Station'] + " "+"to" +" "+df['End Station']
    start_to_end = df['Start To End'].value_counts().idxmax()
    print(f"The most frequent combination of start station and end station trips is {start_to_end}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print(f"the total duration is {total_duration}")

    # TO DO: display mean travel time
    mean_time_duration = round(df['Trip Duration'].mean())
    print(f"the average duration is {mean_time_duration }")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    for index, no_of_users in enumerate(user_type):
        print("  {}: {}".format(user_type.index[index], no_of_users))

    # TO DO: Display counts of gender
    # df (new york and chicago) have "Gender and birth year" columns and df of Washington doesn't has
    # Using if function to check if the df has the Gender Column or not 
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(f"the users types gender are:{gender}")
    else:
        print("No Gender column exists in the df")  


    # TO DO: Display earliest, most recent, and most common year of birth
    # Using if function to check if the df has the "Birth Year" Column or not 
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min().astype('int')
        most_recent = df['Birth Year'].max().astype('int')
        most_common_year = df['Birth Year'].value_counts().idxmax().astype('int')
        print(f"the earliest year is:{earliest}")
        print(f"the most recent year of the birth is: {most_recent}")
        print(f"the most common year of the birth is {most_common_year}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def View_data(df):
    """Displaying  5 rows of the dataframe of the chosen city
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    #create list of user options
    user_reply = ['yes', 'no']
    #user input if display more data is desired
    raw_data = input("If you want to display the data enter \'yes\' if not enter \'no\': ").lower().strip()
    
    ind=5
    while True:
        if raw_data == "yes":
            print(df.iloc[:ind])
            break
        elif raw_data == "no":
            break
        elif raw_data not in user_reply:
            raw_data = input("Invalid input please try again: ")
    
    # get the last index of the dataframe
    last_index=df.index[-1]
    # while loop is used if the user need to display the next 5 rows of the dataframe 
    while raw_data == "yes":
        ind+=5
        raw_data=input("If you need to dispaly more data kindly enter\'yes\' or enter \'no\' if not: ")
        if raw_data == 'yes' and ind < last_index:
            print(df.iloc[ind-5:ind])
        elif ind == last_index:
            print("No more raw data to display")
            break    
        elif raw_data == 'no':
            break  
        elif raw_data not in user_reply:
            raw_data=input("Invalid input enter \'yes\' if you want continue displaying data: ") 

        
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        View_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
