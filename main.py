from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    if sound == 1:
        playsound('alarm 1.mp3')
    elif sound == 2:
        playsound('alarm 2.mp3')
    elif sound == 3:
        playsound('alarm 3.mp3')
    else:
        playsound('alarm 4.mp3')


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes + seconds
sound = int(input("What alarm would you like (1-4): "))

alarm(total_seconds)
