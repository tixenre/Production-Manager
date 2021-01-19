from datetime import datetime, time, timedelta
import csv
#a = (datetime.today() + timedelta(hours=7, minutes=0))
a=datetime.today()
now=a.hour*60+a.minute

bb=13*60
time_of_day=int(bb)

#test list of dic
b = [{'Name': 'Stand Celular Curly', 'Minutes': 110}, {'Name': 'Stand Celular Larry', 'Minutes': '109'}, {'Name': 'Stand Celular Moe', 'Minutes': '129'}]




def write_print_job_scheduled():
    with open("print_jobs_scheduled.csv",'w',newline='') as csv_temp:
        fieldnames = ["Name","Minutes","Hs","Gr","Cm3","Kind","Date"]
        csv_writer = csv.DictWriter(csv_temp, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()

def append_print_job_scheduled(dic):
    with open("print_jobs_scheduled.csv",'a',newline='') as csv_temp:
        fieldnames = ["Name","Minutes","Hs","Gr","Cm3","Kind","Date"]
        csv_writer = csv.DictWriter(csv_temp, fieldnames=fieldnames, delimiter=',')
        csv_writer.writerow(dic)  



def print_scheduler(print_jobs_list):
    jobs_list=[]
    write_print_job_scheduled()
    for i in print_jobs_list:
        t=int(i.get("Minutes"))
        n=i.get("Name")
        evening=(20*60)-time_of_day
        noon=(12*60)-time_of_day
        if time_of_day < 12*60:
            if t< 4*60:
                dic={
                    "Name": n,
                    "Minutes": t,
                    }
                append_print_job_scheduled(dic)
                #jobs_list.append(dic)
                #jobs_list = sorted(jobs_list, key=lambda k: k['Minutes'],reverse=False) 

        elif time_of_day < 20*60:
            if t < evening:
                dic={
                    "Name": n,
                    "Minutes": t,
                    }
                append_print_job_scheduled(dic)
                #jobs_list.append(dic)
                #jobs_list = sorted(jobs_list, key=lambda k: k['Minutes'],reverse=True) 
    
        elif time_of_day >= 20*60:
            if t >= 7*60:
                dic={
                    "Name": n,
                    "Minutes": t,
                    }
                append_print_job_scheduled(dic)
                #jobs_list.append(dic)
                #jobs_list = sorted(jobs_list, key=lambda k: k['Minutes'],reverse=True) 
        else:
            print("Cant find data")
   
    return jobs_list

print(print_scheduler(b))