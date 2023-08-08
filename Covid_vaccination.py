import sqlite3

conn_obj=sqlite3.connect('aadhardetails.db')
cursor_obj= conn_obj.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS VACCINATION")
cursor_obj.execute('''CREATE TABLE VACCINATION(
                   AADHAR_NUM INT PRIMARY KEY NOT NULL,
                   NAME VARCHAR(225),
                   AGE INT,
                   DOSE INT 
);''')
  
# executing data

# aadhar_num = int (input("Enter 12-digit valid Aadhar Number: "))
# rows=cursor_obj.execute("SELECT * FROM AADHAR_DETAIL")
# flag=False
# for row in rows:
#     if aadhar_num == row[0]:
#         name = row[1]
#         age = row[5]
#         dose = int(input('Vaccination dose(s) taken (0 or 1 or 2 or 3):')) 
#         flag = True
#         cursor_obj.execute('''INSERT INTO VACCINATION (AADHAR_NUM, NAME, AGE, DOSE)
#                   VALUES (?, ?, ?, ?)''', (aadhar_num, name, age, dose))

#         data = cursor_obj.execute('''Select * From VACCINATION ''')
#         for row in data :
#             print(row)
            
# if flag == False:  
#     print("invalid aadhar_numbers")  

while True:
    aadhar_num = input("ENTER 5 DIGIT VALID AADHAR NUMBER ")
    ad = cursor_obj.execute("SELECT * FROM AADHAR_DETAIL")
    for row in ad:
        if aadhar_num ==row[0]:
            name = row[1]
            age = row[5]
    dose = input("Vaccination dose(s) taken(0 or 1 or 2): ")
    if dose in [0,1,2]:
        break
    else:
        print("Enter a valid dosage number...")
        continue

cursor_obj.execute('''INSERT INTO VACCINATION(AADHAR_NUM, NAME, AGE, DOSE) VALUES(?, ?, ?, ?)''',(aadhar_num, age, dose))
data = cursor_obj.execute('''SELECT * FROM VACCINATION''')
for row in data:
    print(row)
            
# commit your changes in the database
conn_obj.commit()

#Closing connection
conn_obj.close()
         
  


