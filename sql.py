# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('student.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255));"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Kanon', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('KeKe', 'Data Science', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ren', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Chisato', 'Data Science', 'C')''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()