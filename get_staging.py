from testrailAccount import *
import time
import mysql.connector as mysql
from mysql.connector import Error
import csv
#Import dependencies
from subprocess import call

productList = {
    "xperience" : {
        "productName" : "Xperience",
        "productId" : "7",
        "caseId" : "7"
    },
    "movies" : {
        "productName" : "Movies",
        "productId" : "28",
        "caseId" : "119"
    },
    "bus" : {
        "productName" : "Bus",
        "productId" : "16",
        "caseId" : "16"
    },
    "carRental" : {
        "productName" : "Car Rental",
        "productId" : "24",
        "caseId" : "99"
    },
    "connectivity" : {
        "productName" : "Connectivity",
        "productId" : "8",
        "caseId" : "8"
    },
    "flight" : {
        "productName" : "Flight",
        "productId" : "3",
        "caseId" : "725"
    },
    "eats" : {
        "productName" : "Eats",
        "productId" : "29",
        "caseId" : "1139"
    },
    "hotel" : {
        "productName" : "Hotel",
        "productId" : "4",
        "caseId" : "4"
    },
    "myBooking" : {
        "productName" : "My Booking",
        "productId" : "25",
        "caseId" : "100"
    },
    "paylater" : {
        "productName" : "Paylater",
        "productId" : "21",
        "caseId" : "35"
    },
    "payment" : {
        "productName" : "Payment",
        "productId" : "6",
        "caseId" : "6"
    },
    "shuttle" : {
        "productName" : "Shuttle",
        "productId" : "15",
        "caseId" : "15"
    },
    "train" : {
        "productName" : "Train",
        "productId" : "9",
        "caseId" : "9"
    },
    "trip" : {
        "productName" : "Trip",
        "productId" : "10",
        "caseId" : "10"
    },
    "user" : {
        "productName" : "User",
        "productId" : "5",
        "caseId" : "5"
    },
    "vacation" : {
        "productName" : "Vacation",
        "productId" : "30",
        "caseId" : "127"
    }
}
# Write to CSV
with open('staging.csv', mode='w') as csv_file:
    fieldnames = ['Id', 'Name', 'Total', 'Automated','Percentage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    num=0
    for x in productList:
        cases = client.send_get("get_cases/"+productList[x]["productId"]+"&suite_id="+productList[x]["caseId"])
        i=0
        automated=0
        num+=1
        percentage=0
        testCases=0
        while i<len(cases):
            if (((cases[i]['type_id']==3) and (cases[i]['custom_automation_type']==1)) or (cases[i]['custom_automation_type']==1)):
                automated+=1
            if (cases[i]['custom_test_info']!=5):
                testCases+=1
            i+=1
        percentage = 100 * float(automated)/float(testCases)
        percentage = str(round(percentage,2)) + "%"
        writer.writerow({'Id': num, 'Name': productList[x]['productName'], 'Total': testCases, 'Automated': automated, 'Percentage': percentage})
        print(num, "record inserted\n\n")

#Commit Message
commit_message = "Adding sanity file"

#Stage the file 
call('git add .', shell = True)

# Add your commit
call('git commit -m "'+ commit_message +'"', shell = True)

#Push the new or update files
call('git push origin master', shell = True)