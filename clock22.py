import time
x=input("enter the hour rn 24 hour clock")
hour=int(x)
y=input("enter the min rn")
mins = int(y)
sec = 0
while True:
    print(hour)
    print(mins)
    print("_______________________")
    time.sleep(1)
    sec = sec + 1
    if sec == 59:
        sec = sec - sec
        mins = mins + 1
    elif mins == 59:
        mins = mins - mins 
        hour = hour + 1
    elif hour == 24:
        hour = hour - hour
        mins = mins - mins
        sec = sec - sec
        

     


