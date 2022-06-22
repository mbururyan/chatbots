# Simple IF/ELSE function that will inform user on the time based on the city input by the user

import datetime



while(True):
    city = input('Enter City of choice : ')

    current_time = datetime.datetime.now()

    OG_hour = current_time.hour

    # Set to GMT
    hour = OG_hour - 3

    minute = current_time.minute

    seconds = current_time.second

    # 16 cities to be added

    if city == 'LA':
        hour = hour - 8

    elif city == 'Addis Ababa':
        hour = hour + 3

    elif city == 'NY':
        hour = hour - 5

    elif city == 'Dubai':
        hour = hour + 4

    elif city == 'Texas':
        hour = hour - 6

    elif city == 'Athens':
        hour = hour + 2

    elif city == 'London':
        hour = hour 

    elif city == 'Tokyo':
        hour = hour + 9

    elif city == 'Paris':
        hour = hour + 1

    elif city == 'Hong Kong':
        hour = hour + 9

    elif city == 'Lagos':
        hour = hour + 1

    elif city == 'Rome':
        hour = hour + 1

    elif city == 'Nairobi':
        hour = hour + 3

    elif city == 'Berlin':
        hour = hour + 1

    elif city == 'Rio':
        hour = hour - 3

    elif city == 'Kinshasa':
        hour = hour + 2

    else :
        print('City doesnt exist in our chatbot mate')


    print('Your City is : ', city, 'and the time there right now is', str(hour) + ':' + str(minute) + ':' + str(seconds) )

    break

    
