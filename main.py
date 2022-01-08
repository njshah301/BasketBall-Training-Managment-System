def home_page():
    import front
    import pywebio.output as pwo
    from pywebio.input import input
    pwo.clear() 
    pwo.put_html('''<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1528&q=80');
}

}
</style>
</head>
<body>
</body>
</html>
''' )
    pwo.set_scope('List')
    pwo.put_markdown(""" # Navrang Basketball Academy""")
    pwo.put_markdown(""" ## Insert""")
    pwo.put_buttons(['Insert Contact Information'], onclick = [front.in_info_f])
    pwo.put_buttons(['Insert Player'], onclick = [front.in_player_f])
    pwo.put_buttons(['Insert Trainer'], onclick = [front.in_trainer_f])
    pwo.put_markdown(""" ## Delete""")
    pwo.put_buttons(['Delete Contact Information'], onclick = [front.del_contact_info_f])
    pwo.put_buttons(['Delete Player Information'], onclick = [front.del_player_info_f])
    pwo.put_buttons(['Delete Trainer Information'], onclick = [front.del_trainer_info_f])
    pwo.put_markdown(""" ## Show Table""")
    pwo.put_buttons(['Show Contact Information'], onclick = [front.show_info_f])
    pwo.put_buttons(['Show Player'], onclick = [front.show_player_f])
    pwo.put_buttons(['Show Trainer'], onclick = [front.show_trainer_f])
    pwo.put_markdown(""" ## Search""")
    pwo.put_buttons(['Search Player '], onclick = [front.search_player_f])
    pwo.put_buttons(['Search Contact Information'], onclick = [front.search_contact_f])
    pwo.put_markdown(""" ## Query""")
    pwo.put_buttons(['Average age of Player'], onclick = [front.query5_f])
    pwo.put_buttons(['List all the player names of team who has scored highest points among other teams'], onclick = [front.query1_f])
    pwo.put_buttons(['Find all player’s names who played the highest matches'], onclick = [front.query2_f])
    pwo.put_buttons(['List Date and Court Number for the matches won by team "Panthers"'], onclick = [front.query3_f])
    pwo.put_buttons(['List all the player’s names who played on 22 nd January, 2001 at court No. 12'], onclick = [front.query4_f])
    while(True):
        pass
    
if __name__ == '__main__':
    home_page()
