# Program to greet user using the local timeline
import time 
timestamp = time.strftime("%H:%M:%S")
print (timestamp)
if (timestamp <= 12):
    print ("Good Morning")
elif (timestamp <= 17):
    print ("Good Afternoon") 
elif (timestamp <= 20):
    print ("Good evening")
else :
    print ("Good Night")