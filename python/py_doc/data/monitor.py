import os
import time
import psycopg2
import sys

SQL_QUERY='''
SELECT 
    end_date - start_date as duration 
FROM etl.run_log 
WHERE  process_name= 'etl.fn_etl_ods_to_dw_fact_jurisdiction_crossing' 
ORDER BY run_log_id DESC LIMIT 1
'''
SQL_QUERY = '''
SELECT * FROM pg_stat_activity;
'''
print sys.argv[1]

conn = psycopg2.connect("dbname=xrs_master user=postgres password=postgres")
cur = conn.cursor()
cur.execute(SQL_QUERY)
row = cur.fetchone()
print row
cur.close()
conn.close()
