from datetime import datetime, time, timedelta

#a = (datetime.today() + timedelta(hours=7, minutes=0))
a=datetime.today()
now=a.hour*60+a.minute

bb=20*60
time_of_day=bb

#Urgency
asap= 1
to_print = 2
when_posible = 3



print_jobs2=[15,5,3,60,2*60,2.5*60,3*60,4*60,5*60,6*60,8*60,15*60]

jobs_list=[]


# print(f"Son las {a}")
for t in print_jobs2:
    evening=(20*60)-time_of_day
    noon=(12*60)-time_of_day
    if time_of_day < 12*60:
        if t< 4*60:
            jobs_list.append(t)
            jobs_list.sort()
    
    elif time_of_day < 20*60:
        if t < evening:
            jobs_list.append(t)
            jobs_list.sort(reverse=True)
    
    elif time_of_day >= 20*60:
        if t >= 7*60:
            jobs_list.append(t)
            jobs_list.sort(reverse=True)





print(jobs_list)