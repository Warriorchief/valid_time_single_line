
#solved in a single line
def validTime(time):
    return (time[:2]=='00' or 0<=int(time[:2])<=23) and (time[3:]=='00' or 0<=int(time[3:])<=59)