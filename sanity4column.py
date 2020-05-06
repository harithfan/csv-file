from testrailAccount import *
import time
import mysql.connector as mysql
from mysql.connector import Error
import csv
#Import dependencies
from subprocess import call

productList = {
  "28": "Airport Transfer",
  "26": "Xperience",
  "53": "Bus",
  "31": "Movies",
  "1611": "Cobrand",
  "25": "Connectivity",
  "52": "Eats",
  "32": "Ebill",
  "21": "Flight",
  "22": "Hotel",
  "851": "Insurance",
  "782": "Ipi",
  "1304": "Loyalti",
  "191": "MyBooking",
  "1650": "Paylater Card",
  "33": "Paylater",
  "29": "Payment",
  "23": "Train",
  "27": "Trip",
  "34": "Uangku",
  "1733": "Universal Search",
  "30": "User",
  "862": "Vacation",
  "194": "CarRental",
  "1601": "Visa",
}

# Write to CSV
with open('sanity.csv', mode='w') as csv_file:
    # fieldnames = ['Id', 'Name', 'Total Sanity Test Case', 'Automated','Percentage']
    fieldnames = ['Id', 'Name', 'Total Sanity Test Case', 'Automated', 'Covered(Automatable)', 'Percentage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    num=0
    for x in productList:
        cases = client.send_get("get_cases/20&suite_id="+x)
        i=0
        automated=0
        num+=1
        percentage=0
        coverage=0
        
        while i<len(cases):
            # if (((cases[i]['type_id']==3) and (cases[i]['custom_automation_type']==1)) or (cases[i]['custom_automation_type']==4)):
            if (cases[i]['custom_automation_type']==1):
                coverage+=1
            try:    
                if (len(cases[i]['custom_automation_platform'])!=0):
                    if (cases[i]['custom_automation_type']==1):
                        automated+=1
            except:
                print("no field found")            
            i+=1
        # print("coverage " +str(coverage))
        # print("automated " +str(automated))
        # print("percentage " +str(percentage))
        if ((coverage==0) and (automated==0) or ((coverage==1) and (automated==0))):
            percentage = automated
        else:
            percentage = 100 * (automated)/len(coverage)
            percentage = str(round(percentage,2)) + "%"
        writer.writerow({'Id': num, 'Name': productList[x], 'Total Sanity Test Case': len(cases), 'Automated': automated, 'Covered(Automatable)': coverage, 'Percentage': percentage})
        # writer.writerow({'Id': num, 'Name': productList[x], 'Total Sanity Test Case': len(cases), 'Automated': automated, 'Percentage': percentage})
        print(num, "record inserted\n\n")

#Commit Message
commit_message = "Adding sanity file"

#Stage the file 
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)