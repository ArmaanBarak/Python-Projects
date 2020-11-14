# This program inputs time and initiates a timer.
# While running this program, make sure that script file and sound file are both in the current directory.
# Also, if running from text editor then open the folder inside the text editor where both these files are located


import time
import os
import winsound

def play_alarm():
    '''
    Function to play Alarm
    '''
    
    winsound.PlaySound('sound.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        
def start_timer(hours=0, minutes=0, seconds=0):
    '''
    Function to start timer
    '''
    
    total_time = hours * 3600 + minutes * 60 + seconds

    while total_time != -1:

        try:
            os.system('cls')
        except:
            os.system('clear')

        print('Alarm goes off in: ', end="")

        print(total_time, 'seconds')

        time.sleep(1)

        total_time -= 1

def input_time():
    '''
    Function to input time from user
    '''
    
    while True:

        try:
            res = int(input('What unit of time do you want to set timer for:\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination\n >>> '))
            break
        except:
            print('\nYou gave a wrong input!\nPlease enter a digit\n')

    if res == 1:

        num_of_hours = int(input('Enter number of hours\n >>> '))

        start_timer(hours=num_of_hours)
    
    elif res == 2:

        num_of_minutes = int(input('Enter number of minutes\n >>> '))

        start_timer(minutes=num_of_minutes)

    elif res == 3:

        num_of_seconds = int(input('Enter number of seconds\n >>> '))

        start_timer(seconds=num_of_seconds)

    elif res == 4:

        num_of_hours = int(input('Enter number of hours\n >>> '))

        num_of_minutes = int(input('Enter number of minutes\n >>> '))

        num_of_seconds = int(input('Enter number of seconds\n >>> '))

        start_timer(hours=num_of_hours, minutes=num_of_minutes, seconds=num_of_seconds)

if __name__ == '__main__':
    
    input_time()
    play_alarm()
    input('\nPress Enter to quit.\n')
