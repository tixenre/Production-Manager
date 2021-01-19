from datetime import datetime, time, timedelta

#a = (datetime.today() + timedelta(hours=7, minutes=0))
a=datetime.today()
now=a.hour*60+a.minute

bb=10*60
time_of_day=int(bb)

#test list of dic
b = [{'Name': 'Stand Celular Curly', 'Minutes': 108}, {'Name': 'Stand Celular Larry', 'Minutes': '121'}, {'Name': 'Stand Celular Moe', 'Minutes': '129'}]

def print_scheduler(print_jobs_list):
    for i in print_jobs_list:
        jobs_list=[]
        t=int(i.get("Minutes"))
        n=i.get("Name")
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
        else:
            print("Cant find data")
   
        return jobs_list

