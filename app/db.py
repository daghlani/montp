import sqlite3

def create_conn(db):
   # print("Opened {} database successfully".format(db))
   return sqlite3.connect(db)

def create_tbl(conn):
   # Create table
   # conn.execute('''CREATE TABLE IF NOT EXISTS SERVERS
   #          (ID INTEGER PRIMARY KEY NOT NULL,
   #          IP TEXT    NOT NULL,
   #          TIME        CHAR(100));''')
   conn.execute('''CREATE TABLE IF NOT EXISTS SERVERS
            (IP TEXT PRIMARY KEY NOT NULL,
            TIME        CHAR(100));''')
   print("Table SERVERS created successfully")

def insert(conn,IP,TIME):
   # Insert
   conn.execute("INSERT INTO SERVERS (IP,TIME) VALUES ('{}', '{}')".format(IP,TIME));
   # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
   #    VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
   conn.commit()
   print("Records created successfully")

def select(conn):
   # select
   cursor = conn.execute("SELECT IP, TIME FROM SERVERS")
   res = dict()
   for row in cursor:
      print("IP = ", row[0])
      print("TIME = ", row[1], "\n")
      res[row[0]] = row[1]

   print("Operation done successfully")
   return(res)

def selectSp(conn, IP):
   # select
   cursor = conn.execute("SELECT IP, TIME FROM SERVERS WHERE IP = '{}'".format(IP))
   res = ''
   for row in cursor:
      print("IP = ", row[0])
      print("TIME = ", row[1], "\n")
      res = row[1]

   print("Operation done successfully")
   return(res)

def update(conn, IP, TIME):
   # update 
   conn.execute("UPDATE SERVERS set TIME = {} where IP = {}".format(IP,TIME))
   conn.commit()
   print("Total number of rows updated :", conn.total_changes)


# def delete(conn):    
#    # delete
#    conn.execute("DELETE from SERVERS where ID = 2;")
#    conn.commit()
#    print("Total number of rows deleted :", conn.total_changes)


def inOrup(conn, IP, TIME):
   # conn.execute("INSERT OR REPLACE INTO SERVERS (IP, TIME) \
   # values ((SELECT ID FROM SERVERS WHERE IP = '{}'),'{}','{}');".format(
   #    IP, IP, TIME
   # ))
   conn.execute("INSERT OR IGNORE INTO SERVERS (IP, TIME) VALUES ('{}', '{}')".format(IP, TIME))
   conn.execute("UPDATE SERVERS SET TIME = '{}' WHERE IP = '{}'".format(TIME, IP))
   conn.commit()
   print("Record {} create or updated".format(IP))


def get_servers_asc(conn):
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM `SERVERS` ORDER BY TIME ASC")
   results = cursor.fetchall()
   return results

def get_servers_desc(conn):
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM `SERVERS` ORDER BY TIME DESC")
   results = cursor.fetchall()
   return results

def exxec(conn, query):
   conn.execute(query)
   conn.commit()