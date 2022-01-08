import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Setting auto commit false
conn.autocommit = True
def in_info(mail, address, m1, m2 ,des):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True

    temp='''INSERT INTO "Sports_Training"."Contact_Information"(
	"Mail_ID", "Address", "Mobile_Number1", "Mobile_Number2", "Designation")
	VALUES (%s, %s, %s, %s, %s);'''
    data=[(mail,address,m1,m2,des)]
    try:
        cursor.executemany(temp, data)
        return 0
    except:
        return -1
    #Commit your changes in the database

def in_player(pid,fid,mid,h,name,pos,dob, pw, att, pstatus,age):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    temp= '''INSERT INTO "Sports_Training"."Player"(
	"Player_ID", "Fee_Structure_ID", "Mail_ID", "Height", "Name", "Position", "Birth_Date", "Password", "Attendance", "Player_Status", "Age")
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    data=[(pid,fid,mid,h,name,pos,dob, pw, att, pstatus,age)]
    try:
        cursor.executemany(temp, data)
        return 0
    except:
        return -1
        
def in_trainer(tid,mid,ssid,name,pw,att):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    temp='''INSERT INTO "Sports_Training"."Trainer"(
	"Trainer_ID", "Mail_ID", "Salary_Structure_ID", "Name", "Password", "Attendance")
    VALUES (%s, %s, %s, %s, %s, %s);'''
    data=[(tid,mid,ssid,name,pw,att)]
    try:
        cursor.executemany(temp, data)
        return 0
    except:
        return -1

def del_contact_info(mid):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    s = "DELETE FROM \"Sports_Training\".\"Contact_Information\" WHERE \"Mail_ID\"='{}';".format(mid)
    print(s)
    #Deleting records
    try:
        cursor.execute(s)
        print(cursor.rowcount)
        if(cursor.rowcount):
            return 0
        return -1
    except:
        return -1

def del_player_info(pid):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    s="DELETE FROM \"Sports_Training\".\"Player\" WHERE \"Player_ID\"='{}';".format(pid)
    #Deleting records
    try:
        cursor.execute(s)
        print(cursor.rowcount)
        if(cursor.rowcount):
            return 0
        return -1
    except:
        return -1
        
def del_trainer_info(tid):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    s = "DELETE FROM \"Sports_Training\".\"Trainer\" WHERE \"Trainer_ID\"='{}';".format(tid)
    print(s)
    #Deleting records
    try:
        cursor.execute(s)
        print(cursor.rowcount)
        if(cursor.rowcount):
            return 0
        return -1
    except:
        return -1

def query1(): #query 31 List all the player names of team who has scored highest points among other teams.
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute(''' Select "Name"
    From "Sports_Training"."Player"
    Where "Player_ID" in
    (Select "Player_ID"
    From "Sports_Training"."Association"
    where "Team_ID"=
    (Select "Team_ID"
    From "Sports_Training"."Team"
    Where "Team_Points"=(Select max("Team_Points")
    From "Sports_Training"."Team"))) and "Player_Status"='Active'  ''')
    result = cursor.fetchall();
    result.insert(0, ('Name',)); 
    return result
    
    
def query2(): #query 27
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute(''' select distinct "Name"
    from "Sports_Training"."Player"
    natural join "Sports_Training"."Association"
    where "Matches_Played" =(select max("Matches_Played")
	from "Sports_Training"."Association")''')
    result = cursor.fetchall();
    result.insert(0, ('Name',)); 
    return result

def query3(): #query 32
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute(''' select "Date", "Court_Number"
    from ("Sports_Training"."Team" natural join "Sports_Training"."Team_Match" natural join "Sports_Training"."Matches" natural join "Sports_Training"."Training_Session") as rec
    where "Winning_Team_Name" = 'Panthers'
    group by "Court_Number", "Date"
    order by "Date" ''')
    result = cursor.fetchall();
    result.insert(0,('Date' , 'Court_Number'));
    return result

def query4(): #query 35
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute(''' Select "Name"
    From "Sports_Training"."Player"
    Where "Player_ID" in(Select "Player_ID"
    From "Sports_Training"."Schedule_Player"
    Where "Session_ID"=(Select "Session_ID"
    From "Sports_Training"."Training_Session"
    Where "Date"='22-01-2021' and "Court_Number"=12))''')
    result = cursor.fetchall();
    result.insert(0, ('Name',)); 
    return result
    
def query5(): 
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute(''' select round(avg("Age"),2) from "Sports_Training"."Player"''')
    result = cursor.fetchall();
    result.insert(0, ('Average Age',)); 
    return result

def show_info():
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute('''SELECT * FROM "Sports_Training"."Contact_Information";''')
    result = cursor.fetchall();
    result.insert(0, ('Mail_ID', 'Address', 'Mobile_Number1', 'Mobile_Number2', 'Designation'));
    return (result)

def show_player():
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute('''SELECT * FROM "Sports_Training"."Player";''')
    result = cursor.fetchall();
    result.insert(0, ('Player_ID', 'Fee_Structure_ID', 'Mail_ID', 'Height', 'Name', 'Position ', 'Birth_Date' , 'Password' , 'Attendance' , 'Player_Status' , 'Age'));
    return (result)

def show_trainer():
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute('''SELECT * FROM "Sports_Training"."Trainer";''')
    result = cursor.fetchall();
    result.insert(0, ('Trainer_ID', 'Mail_ID', 'Salary_Structure_ID', 'Name', 'Password' , 'Attendance' ));
    return (result)

def search_player(p_id):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    s = 'Select * From "Sports_Training"."Player" Where "Player_ID"=\'{}\';'.format(p_id)
    print(s)
    try:
        cursor.execute(s)
        ans = cursor.fetchall()
        ans.insert(0, ('Player_ID', 'Fee_Structure_ID', 'Mail_ID', 'Height', 'Name', 'Position ', 'Birth_Date' , 'Password' , 'Attendance' , 'Player_Status' , 'Age'));
        return ans
    except:
        return -1

def search_contact(mail_id):
    conn = psycopg2.connect(database="Basketball", user='postgres', password='admin', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    conn.autocommit = True
    s = 'Select * From "Sports_Training"."Contact_Information" Where "Mail_ID"=\'{}\';'.format(mail_id)
    print(s)
    try:
        cursor.execute(s)
        ans = cursor.fetchall()
        ans.insert(0, ('Mail_ID', 'Address', 'Mobile number 1', 'Mobile number 2', 'Designation'));
        return ans
    except:
        return -1



conn.commit()

# Closing the connection
conn.close()
# Connection esta