# import libraries
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
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name.")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? (all, january, february, march, april, may, june)\n").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid input. Please enter a valid month name.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day? (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid input. Please enter a valid day of the week.")

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
    # Load data file into dataframe for the specified city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columuns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month !='all':
        #Use the index of the months list to get the correspeonding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new DataFrame
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new DataFrame
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f'Most Common Month: {popular_month}')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f'Most Common Day of Week: {popular_day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'Most Common Start Hour: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'Most Commonly Used Start Station: {common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'Most Commonly Used End Station: {common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'Most Frequent combination of Start and End Station: {common_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total Travel time: {total_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean Travel Time: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print(f'User Types: {user_types}')

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print(f'Gender Counts: {gender_counts}')
    except KeyError:
        print('Gender data is not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print(f'Earliest Year of Birth: {earliest_year}')
        print(f'Most Recent Year of Birth: {most_recent_year}')
        print(f'Most Common Year of Birth: {most_common_year}')
    except KeyError:
        print('Birth Year data is not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Displays 5 rows of data at a time upon user request."""
    start_loc = 0
    view_data = input('Would you like to view the first 5 rows of the data? Enter yes or no.\n')
    while view_data.lower() == 'yes':
        print(df.head(5))
        df = df.iloc[5:]  # Update df to the next 5 rows
        view_data = input('Do you wish to continue? Enter yes or no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
