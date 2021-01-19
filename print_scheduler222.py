from datetime import datetime, timedelta


d = (datetime.today() + timedelta(hours=7, minutes=0)).strftime('%H:%M')

#now=datetime.datetime.now().time()
#Urgency
asap= 1
to_print = 2
when_posible = 3

#Day time priority
#morning= datetime.time(9)
#night= datetime.time(20)


#

print_jobs=["0.5","8","6","2","15","1.5"]

late_print_job_list=[]
morning_print_job_list=[]

jobs_list=[]
# for t in print_jobs:
#     tt=t.strftime('%H:%M %p')
#     if t > d:
#         jobs_list.append(t)


        
# for t in print_jobs:
#     if t >= 8:
#         morning_print_job_list.append(t)
#     else:
#         late_print_job_list.append(t)

#     pass

print(jobs_list)

