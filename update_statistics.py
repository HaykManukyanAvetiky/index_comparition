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

    query = f"update {table_name} set scan_id = %s , issue_flag = %s, sequence = %s where id = %s "


    with open(f"{table_name}_update.csv", 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['query_type','duration'])

        for i in range(1,2000):
            id = random.randint(1,45000000)
            scan = random.randint(0,10000)
            issue_flag = random.randint(0,200)
            sequence = random.randint(0,5000)
            start = datetime.datetime.now()
            cur.execute(query, (scan, sequence, issue_flag, id) )
            end = datetime.datetime.now()
            dur = (end - start).total_seconds()
            print('update_seq_scan_issue_by_id', dur , id )
            spamwriter.writerow(['update_seq_scan_issue_by_id', dur])
    cur.close()
    conn.close()


if __name__ == '__main__':
    table_names =  ['data_table', 'data_table']
    [collect_stat(table_name) for table_name in table_names ]