from testrailAccount import *
import time
import mysql.connector as mysql
from mysql.connector import Error
import csv

productList = {
  "28": "Airport Transfer",
  "26": "Experience",
  "53": "Bus",
  "31": "Cinema",
  "25": "Connectivity",
  "52": "Eats",
  "32": "Ebill",
  "21": "Flight",
  "22": "Hotel",
  "851": "Insurance",
  "782": "Ipi",
  "1304": "Loyalti",
  "191": "MyBooking",
  "33": "Paylater",
  "29": "Payment",
  "23": "Train",
  "27": "Trip",
  "34": "Uangku",
  "30": "User",
  "862": "Vacation",
  "194": "CarRental",  
}

tbl = "tblSanity"

# db = mysql.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "tvlk",
#     database = "dashboard",
#     port='3306'
# )

# cursor = db.cursor()
# deleteTbl = "DROP TABLE "+ tbl;
# cursor.execute(deleteTbl)

# createTbl = "CREATE TABLE "+ tbl +" ( \
#         id int(10) NOT NULL AUTO_INCREMENT, \
#         product_name varchar(300), \
#         total_test int(5), \
#         automated int(5), \
#         PRIMARY KEY(id))"
# cursor.execute(createTbl)

# Write to CSV
with open('sanity.csv', mode='w') as csv_file:
    fieldnames = ['Id', 'Name', 'Total', 'Automated','Percentage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    num=0
    for x in productList:
        cases = client.send_get("get_cases/20&suite_id="+x)
        i=0
        automated=0
        num+=1
        percentage=0
        
        while i<len(cases):
            if (((cases[i]['type_id']==3) and (cases[i]['custom_automation_type']==1)) or (cases[i]['custom_automation_type']==4)):
                automated+=1
            i+=1
        percentage = 100 * float(automated)/float(len(cases))
        percentage = str(round(percentage,2)) + "%"
        writer.writerow({'Id': num, 'Name': productList[x], 'Total': len(cases), 'Automated': automated, 'Percentage': percentage})
        print(num, "record inserted\n\n")

# try:
#     query = "SELECT id,product_name AS product_name,\
#              automated,\
#              total_test,\
#              concat(round((automated/total_test * 100),2), '%') as percentage\
#       FROM `tblSanity`\
#       GROUP BY id\
#       ORDER BY percentage DESC";
#     cursor = db.cursor()
#     cursor.execute(query)
#     records = cursor.fetchall()
#     print("Total number of rows is: ", cursor.rowcount)
#     print("\nPrinting each laptop record")
    
#     # Write to CSV
#     with open('sanity.csv', mode='w') as csv_file:
#         fieldnames = ['Id', 'Name', 'Total', 'Automated','Percentage']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#         for row in records:
#             writer.writerow({'Id': row[0], 'Name': row[1], 'Total': row[2], 'Automated': row[3], 'Percentage': row[4]})
# except Error as e:
#     print("Error reading data from MySQL table", e)
# finally:
#     if (db.is_connected()):
#         db.close()
#         cursor.close()
#         print("MySQL connection is closed")



# for x in productList:
#     cases = client.send_get("get_cases/20&suite_id="+x)
#     i=0
#     automated=0
#     while i<len(cases):
#         if (((cases[i]['type_id']==3) and (cases[i]['custom_automation_type']==1)) or (cases[i]['custom_automation_type']==4)):
#             automated+=1
#         i+=1
#     query = "INSERT INTO " + tbl + " (product_name, total_test, automated) VALUES (%s, %s, %s)"
#     values = (productList[x], len(cases), automated)
#     cursor.execute(query, values)
#     db.commit()
#     print(cursor.rowcount, "record inserted\n\n")

# try:
#     query = "SELECT id,product_name AS product_name,\
#              automated,\
#              total_test,\
#              concat(round((automated/total_test * 100),2), '%') as percentage\
#       FROM `tblSanity`\
#       GROUP BY id\
#       ORDER BY percentage DESC";
#     cursor = db.cursor()
#     cursor.execute(query)
#     records = cursor.fetchall()
#     print("Total number of rows is: ", cursor.rowcount)
#     print("\nPrinting each laptop record")
    
#     # Write to CSV
#     with open('sanity.csv', mode='w') as csv_file:
#         fieldnames = ['Id', 'Name', 'Total', 'Automated','Percentage']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#         for row in records:
#             writer.writerow({'Id': row[0], 'Name': row[1], 'Total': row[2], 'Automated': row[3], 'Percentage': row[4]})
# except Error as e:
#     print("Error reading data from MySQL table", e)
# finally:
#     if (db.is_connected()):
#         db.close()
#         cursor.close()
#         print("MySQL connection is closed")