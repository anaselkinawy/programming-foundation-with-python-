import webbrowser
import time
total_breaks= 3
break_count = 0
#making a loop to repeat taking break 3 times
while (break_count < total_breaks) :
    #time befor each start to break
    time.sleep(3*60*60)
    #opening the url we want
    webbrowser.open("https://www.youtube.com/")
    #increasing the break_count by one
    break_count +=1

