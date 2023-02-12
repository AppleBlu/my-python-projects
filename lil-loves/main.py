# Importing modules
from dates_database import dates
from art import logo

# Gender preference list to be checked against later
preferences = ['male', 'female', 'both']

male_profiles = ['micheal', 'jim', 'kevin', 'dwight']
female_profiles = ['pam', 'angela', 'jan', 'phillis']
joint_profiles = ['micheal', 'pam', 'kevin', 'angela', 'jim', 'phillis', 'dwight', 'jan']

is_single = False


class User:

    def __init__(self, name, age, gender, gender_preference):
        self.name = name
        self.age = age
        self.gender = gender
        self.gender_preference = gender_preference


def format_date_profile(profile):
    """Formats a dating profile in a more readable string"""
    age = dates[profile][0]
    gender = dates[profile][1]
    hobbies = dates[profile][2]
    return f'{profile}\n--------\nA {gender} aged {age} who likes to {hobbies}'


# Welcome message
print(logo)
print('\nWelcome to LIL LOVES!!!\n\nPlease register below:')

# Asking if you are single
single = input('------------------------\nAre you single? (Y/N): ').lower()
# Checking answer
if single == 'n':
    print('Right answer haha. Guess you will not be needing this service\nGoodBye')
    is_single = True

# While loop while user is single
while not is_single:
    # Asking user for credentials
    user_name = input('Name: ').title()
    user_age = int(input('age: '))
    if user_age < 18:
        print('To young sorry')
        exit()
    elif user_age > 50:
        print('To old sorry')
        exit()
    user_gender = input('Gender: ')
    print('Is your gender preference Male, female or both?')
    user_gender_preference = input('Preference: ').lower()

    # While loop while user has an invalid input
    while user_gender_preference not in preferences:
        print('Please enter male, female or both')
        user_gender_preference = input('Preference: ').lower()

    # Object user
    user = User(user_name, user_age, user_gender, user_gender_preference)

    # Break before showing user profiles
    print('\nThank you for registering\n')
    input('Press enter to find your soulmate!')


    def swipe(profile_list):
        for profile in profile_list:
            title_profile = profile.title()
            print('\n')
            print(format_date_profile(profile).title())
            user_swipe = input('\nL Swipe R\nSwipe: ').lower()

            while user_swipe != 'l' and user_swipe != 'r':
                user_swipe = input('\nL Swipe R\nSwipe: ').lower()

            if user_swipe == 'l':
                print(f'\nYou and {title_profile} will live happily ever after <3')
                print(logo)
                exit()
        swipe(profile_list)


    if user.gender_preference == 'both':
        swipe(joint_profiles)
    elif user_gender_preference == 'male':
        swipe(male_profiles)
    elif user_gender_preference == 'female':
        swipe(female_profiles)
