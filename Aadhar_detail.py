import sqlite3

#Connection creation
conn_obj=sqlite3.connect('aadhardetails.db')

#cursor object creation
cursor_obj = conn_obj.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS AADHAR_DETAIL")

# table creation
table = '''CREATE TABLE AADHAR_DETAIL(
                           AADHAR_NUM INT PRIMARY KEY NOT NULL,
                           NAME VARCHAR(225) NOT NULL,
                           ADDRESS VARCHAR(225),
                           PHONE_NUM INT,
                           GENDER CHAR,
                           AGE INT
)'''
cursor_obj.execute(table)

#Data insertion
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666671','DARSHU','MYSORE','7892354591','FEMALE','22')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666672','SANJU','BANGLORE','7892354592','MALE','24')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666673','VARSHA','DAVANGERE','7892354593','FEMALE','21')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666674','DEVA','MANDYA','7892354594','MALE','25')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666675','SINCHU','MYSORE','7892354595','FEMALE','27')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666676','MANOJ','TUMKUR','7892354596','MALE','29')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666677','AVI','RAMANAGAR','7892354597','MALE','21')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666678','MADAN','CHANNAPATNA','7892354598','MALE','23')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666679','SANJANA','MADIKERI','7892354599','FEMALE','26')''')
cursor_obj.execute('''INSERT INTO AADHAR_DETAIL VALUES('512781666670','DARSHINI','HASSAN','7892354590','FEMALE','28')''')

#Query excution
res = cursor_obj.execute('''SELECT * FROM AADHAR_DETAIL''')
print("Data Inserted Successfully")
for row in res:
    print(row)
    
# commit your changes in the database
conn_obj.commit()

# closing the connection
conn_obj.close()  

