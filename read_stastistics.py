#!/usr/bin/python

import datetime
import csv
import psycopg2 as pg
import random


def collect_stat(table_name):

    con_set = {
    'host': 'localhost',
    'port': 5438,
    'database' : 'rainbow_database',
    'user': 'unicorn_user',
    'password' : 'magical_password'
    }

    conn = pg.connect(**con_set)
    cur = conn.cursor()

    queries = {
        'scan_id' : f"Select * from {table_name} where job = %s and nlp = %s and year = %s and scan_id = %s",  
        'issue_flag': f"Select * from {table_name} where job = %s and nlp = %s and year = %s and  issue_flag = %s",  
        'sequence': f"Select * from {table_name} where job = %s and nlp = %s and year = %s and  sequence = %s" 
    }

    with open(f"{table_name}_read.csv", 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['query_type','duration'])

        for i in range(1,2):
            nlp = random.randint(0,20)
            year = random.randint(0,15)
            job = random.randint(0,30)
            var4 = {
                'scan_id' : random.randint(0,10000),
                'issue_flag' : random.randint(0,200),
                'sequence' : random.randint(0,5000) 
            }
            for pair in queries.items():
                start = datetime.datetime.now()
                cur.execute(pair[1], (job, nlp, year, var4[pair[0]]) )
                end = datetime.datetime.now()
                dur = (end - start).total_seconds()
                print(pair[0], dur )
                spamwriter.writerow([pair[0], dur])
    cur.close()
    conn.close()


if __name__ == '__main__':
    table_names =  ['data_table', 'data_table']
    [collect_stat(table_name) for table_name in table_names ]