from back import *
import pywebio.output as pwo
from pywebio.input import *
from main import *

#del - https://ibb.co/BPpfy40
def in_info_f():
    pwo.clear()
    arr = input_group("Insert Contact Information",[
    input('Mail_ID', name='name'),
    input('Address', name='addrs'),
    input('Mobile Number 1', name='m1'),
    input('Mobile Number 2', name='m2'),
    input('Designation', name='desig')])
    isSuccessful = in_info(str(arr['name']), str(arr['addrs']), str(arr['m1']), str(arr['m2']), str(arr['desig']))
    if(isSuccessful == -1):
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    else:
        img=open("inset_successful_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def in_player_f():
    pwo.clear()
    arr = input_group("Insert Player Information",[
    input('Player_ID', name='1'),
    input('Fee_Structure_ID', name='2', type=NUMBER),
    input('Mail_ID', name='3'),
    input('Height', name='4'),
    input('Name', name='5'),
    input('Position', name = '6'),
    input('Birth_Date', name = '7', type=DATE),
    input('Password', name='8', type = PASSWORD),
    input('Attendance', name='9'),
    input('Player_Status', name='10')])
    arr['11'] = 0
    isSuccessful = in_player(arr['1'], arr['2'], arr['3'], arr['4'], arr['5'], arr['6'], arr['7'], arr['8'], arr['9'], arr['10'], arr['11'])
    if(isSuccessful == -1):
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    else:
        img=open("inset_successful_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
    
def in_trainer_f():
    pwo.clear()
    arr = input_group("Insert Trainer Information",[
    input('Trainer_ID', name='1'),
    input('Mail_ID', name='2'),
    input('Salary_Structure_ID', name='3', type=NUMBER),
    input('Name', name='4'),
    input('Password', name='5', type = PASSWORD),
    input('Attendance', name='6', type = FLOAT)])
    isSuccessful = in_trainer(arr['1'], arr['2'], arr['3'], arr['4'], arr['5'], arr['6'])
    if(isSuccessful == -1):
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    else:
        img=open("inset_successful_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def del_contact_info_f():
    pwo.clear()
    s = input("Insert Primary key: ")
    del1 = del_contact_info(s)
    if(del1 == -1):
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    else:
        img=open("delete_successful_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def del_player_info_f():
    pwo.clear()
    s = input("Insert Primary key: ")
    del1 = del_player_info(s)
    if(del1 == -1):
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    else:
        img=open("delete_successful_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def del_trainer_info_f():
    pwo.clear()
    s = input("Insert Primary key: ")
    del1 = del_trainer_info(s)
    if(del1 == -1):
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    else:
        img=open("delete_successful_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def show_info_f():
    pwo.clear()
    txt = show_info()
    pwo.put_markdown(""" # Contact Information""")
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def show_player_f():
    pwo.clear()
    txt = show_player()
    pwo.put_markdown(""" # Player""")
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def show_trainer_f():
    pwo.clear()
    txt = show_trainer()
    pwo.put_markdown(""" # Trainer""")
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def search_player_f():
    pwo.clear()
    p_id=int(input("Enter Player_ID"))
    ans=search_player(p_id);
    if(ans!=-1):
        pwo.put_markdown(""" # Player Information""")
        
        pwo.put_table(ans)
    elif ans==-1:
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def search_contact_f():
    pwo.clear()
    mail_id=input("Enter Mail_ID")
    ans=search_contact(mail_id);
    if(ans!=-1):
        pwo.put_markdown(""" # Contact Information""")
        pwo.put_table(ans)
    elif ans==-1:
        img=open("something-went-wrong_f.gif",'rb').read()
        pwo.put_image(img)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def query1_f():
    pwo.clear()
    txt = query1() 
    pwo.put_markdown(""" # List all the player names of team who has scored highest points among other teams.""")
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def query2_f():
    pwo.clear()
    txt = query2()
    pwo.put_markdown(""" # Find all player's names who played the highest matches.""")
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])

def query3_f():
    pwo.clear()
    txt = query3() 
    pwo.put_markdown(""" # List Date and Court Number for the matches won by team "Panthers".""")
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])

def query4_f():
    pwo.clear()
    txt = query4() 
    pwo.put_markdown(""" # List all the player's names who played on 22 nd January, 2001 at court No. 12.""")
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
    
def query5_f():
    pwo.clear()
    txt = query5() 
    pwo.put_markdown(""" # Find the Average Age of all Player. """)
    pwo.put_table(txt)
    pwo.put_buttons(['Home Page'], onclick = [home_page])
