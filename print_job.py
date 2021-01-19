import csv

def print_job_generator():
        with open("parsed.csv", 'r') as print_jobs:
            csv_data = csv.DictReader(print_jobs)
            lis=[]
            
            for line in csv_data:
                dic={
                    "Name": line.get("Name"),
                    "Minutes": line.get("Minutes"),
                    }

                lis.append(dic)
        return lis

#print(print_job_generator())