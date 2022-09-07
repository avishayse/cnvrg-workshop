First of all you have to start your xamp server


### Install Package

```
pip install mysql-connector-python
```

### Connection Establishment Code 

```python
# import package
import mysql.connector

#database connection
db = mysql.connector.connect(host='localhost',database='test',user='root',password='')

'''
Your code here...
'''

# disconnect from server
db.close()

```

### Create Table

```python
# import package
import mysql.connector

#database connection
db = mysql.connector.connect(host='localhost',database='test',user='root',password='')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()

```

### Insert Table

```python
# import package
import mysql.connector

#database connection
db = mysql.connector.connect(host='localhost',database='test',user='root',password='')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   
# disconnect from server
db.close()

```
### Read Operation

* fetchone() − It fetches the next row of a query result set. A result set is an object that is returned when a cursor object is used to query a table.

* fetchall() − It fetches all the rows in a result set. If some rows have already been extracted from the result set, then it retrieves the remaining rows from the result set.

* rowcount − This is a read-only attribute and returns the number of rows that were affected by an execute() method.


```python
# import package
import mysql.connector

#database connection
db = mysql.connector.connect(host='localhost',database='test',user='root',password='')

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()

```
### Update Operation

```python
# import package
import mysql.connector

#database connection
db = mysql.connector.connect(host='localhost',database='test',user='root',password='')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
                          WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

```

### Delete Operation

```python
# import package
import mysql.connector

#database connection
db = mysql.connector.connect(host='localhost',database='test',user='root',password='')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

```