##    https://www.hackerrank.com/challenges/time-conversion/problem

##    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

##### ##### ##### #####

#   O(1)
#   String slicing

def solutionOne(time_string):

    hour = int(time_string[:2])

    if time_string[-2] == 'A':

        if hour == 12:
            new_time_string = ('00' + time_string[2:8])
            
        else:
            new_time_string = time_string[:8]

    else:

        if hour == 12:
            new_time_string = time_string[:8]

        else:
            hour += 12
            new_time_string = (str(hour) + time_string[2:8])

    return new_time_string
