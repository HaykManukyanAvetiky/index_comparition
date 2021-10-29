
import psycopg2 as pg
import random
import string   

con_set = {
    'host': 'localhost',
    'port': 5438,
    'database' : 'rainbow_database',
    'user': 'unicorn_user',
    'password' : 'magical_password'
}


conn = pg.connect(**con_set)
conn.autocommit = False

for i in range(1,5000): 
    cur = conn.cursor()
    for j in range(1,10000):
        nlp = random.randint(0,5000)
        year = random.randint(0,200)
        job = random.randint(0,10000)
        scan = random.randint(0,10000)
        issue_flag = random.randint(0,200)
        sequence = random.randint(0,5000)
        img_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
        
        cur.execute("""insert into test(job,nlp,year,scan_id,issue_flag,sequence,img_name) 
                    VALUES (%s , %s , %s , %s , %s , %s , %s )""", 
                    (job,nlp,year,scan,issue_flag,sequence,img_name  ))
    conn.commit()
    cur.close()
    print('batch   ', i)


