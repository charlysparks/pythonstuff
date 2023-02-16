import time
from datetime import timedelta

# Set the length of time for each work period and break period
WORK_TIME = timedelta(minutes=25)
BREAK_TIME = timedelta(minutes=5)

# Define a function to start the timer
def start_timer(timer_type):
    if timer_type == "work":
        time_left = WORK_TIME
        message = "Time to work!"
    elif timer_type == "break":
        time_left = BREAK_TIME
        message = "Time for a break!"

    while time_left:
        # Clear the console screen
        print(chr(27) + "[2J")
        # Print the time remaining
        minutes, seconds = divmod(time_left.seconds, 60)
        print(f"{message}\n{minutes:02d}:{seconds:02d}")
        # Sleep for 1 second
        time.sleep(1)
        # Subtract 1 second from the time remaining
        time_left -= timedelta(seconds=1)

    # Clear the console screen and print a message when the timer is done
    print(chr(27) + "[2J")
    if timer_type == "work":
        print("Great job! Time for a break.")
        start_timer("break")
    elif timer_type == "break":
        print("Time to get back to work!")
        start_timer("work")

# Start the timer with a work period
start_timer("work")

