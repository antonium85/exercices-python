#Marathon Time Calucultor - www.101computing.net/marathon
import datetime

#Step 1: INPUT: Ask the runner for their pace (e.g. 5:25)
str_pace = input("At what pace do you run a km? e.g. 5:21 ")

#Step 2: PROCESS: Convert this input into a number of seconds: e.g. 5:25 = 5 * 60 + 25 = 325 seconds
#...
minute, second = str_pace.split(':')
int_pace = int(minute) * 60 + int(second)

#Step 3: PROCESS: Multiply this total by 42 as there are 42km in a Marathon
#...
total_time = int_pace * 42

#Step 4: PROCESS: Convert this new total using the hh:mm:ss format. (e.g 3:47:30)
#...
#hour, minute, second = int(total_time / 3600), int((total_time%3600)/60), int((total_time%3600)%60)
time_object = datetime.timedelta(seconds=total_time)

#Step 5: OUTPUT: Display this new total on screen (using the hh:mm:ss format). (e.g 3:47:30)
#...
print(time_object)
