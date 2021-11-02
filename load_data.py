#!/usr/bin/python

import threading
import psycopg2 as pg
import random
import string   


def load_data(job, nlp, year):
    con_set = {
    'host': 'localhost',
    'port': 5438,
    'database' : 'rainbow_database',
    'user': 'unicorn_user',
    'password' : 'magical_password'
    }
    conn = pg.connect(**con_set)
    conn.autocommit = False
    cur = conn.cursor()
    for _ in range(1,5000):
        scan = random.randint(0,10000)
        issue_flag = random.randint(0,200)
        sequence = random.randint(0,5000)
        img_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
        print(job,nlp,year,scan,issue_flag,sequence,img_name  )
        cur.execute("""insert into data_table(job,nlp,year,scan_id,issue_flag,sequence,img_name) 
                    VALUES (%s , %s , %s , %s , %s , %s , %s )""", 
                    (job,nlp,year,scan,issue_flag,sequence,img_name  ))
    conn.commit()
    cur.close()
    print('job ', job, 'nlp ', nlp, 'year ', year)



for job in range(1,30):
    for nlp in range(1,20):
        threads = []
        for year in range(1,15):
            threads.append(threading.Thread(target=load_data, args=(job, nlp, year)))
        [ x.start() for x in threads]  
        [ x.join() for x in threads]  



# for i in range(1,5000): 
#     cur = conn.cursor()
#     for j in range(1,10000):
#         nlp = random.randint(0,5000)
#         year = random.randint(0,200)
#         job = random.randint(0,10000)
#         scan = random.randint(0,10000)
#         issue_flag = random.randint(0,200)
#         sequence = random.randint(0,5000)
#         img_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
        
#         cur.execute("""insert into test(job,nlp,year,scan_id,issue_flag,sequence,img_name) 
#                     VALUES (%s , %s , %s , %s , %s , %s , %s )""", 
#                     (job,nlp,year,scan,issue_flag,sequence,img_name  ))
#     conn.commit()
#     cur.close()
#     print('batch   ', i)


