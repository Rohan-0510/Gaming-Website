import psycopg2
import json
from sys import argv

data_before = {}
data_after = {}

def write_in_json_before(data):
    try:
        with open("before_access_fda_report.json","w") as report:
            json.dump(data,report)
            print("record added")
    except FileNotFoundError:
        print("File not found..")

def before_access_fda_report():
    try:
        con = psycopg2.connect(host="localhost",database="demodb",port="5432",user="postgres",password="123456")
        cur = con.cursor()

        cur.execute("select count(*) from applications")
        count = cur.fetchone()[0]
        print("Count=", count)
        cur.execute("select appltype, count(*) from applications group by appltype")
        rows = cur.fetchall()
        data_before['Applications'] = count
        data_before['Appltype'] = dict(rows)

        cur.execute("select count(*) from products")
        count = cur.fetchone()[0]
        print("Count=", count)
        data_before['Products'] = count

        cur.execute("select count(*) from submissions")
        count = cur.fetchone()[0]
        print("Count=", count)
        data_before['Submission'] = count
        write_in_json_before(data_before)
        cur.close()

    except Exception as e:
        print("Exception issue-->",e)

    finally:
        if con is not None:
            con.close()


def open_file():
    fopen = open('before_access_fda_report.json',)
    data_before_refresh = json.load(fopen)
    return data_before_refresh

def write_in_json(data):
    try:
        with open("after_access_fda_report.json","w") as report:
            json.dump(data,report)
            print("record added")
    except FileNotFoundError:
        print("File not found..")

def after_access_fda_report():
    try:
        con = psycopg2.connect(user = "root",password = "sMXdGP4KH2Gp9pCg",host = "ria-postgresql-db-dev.c8lzkpuhg1fd.us-east-1.rds.amazonaws.com",port = "5432",database = "regintan_dev")
        cur = con.cursor()

        cur.execute("select count(*) from fda_staging.applications")
        count = cur.fetchone()[0]
        print("Count=" , count)
        cur.execute("select appltype, count(*) from fda_staging.applications group by appltype")
        rows = cur.fetchall()
        data_before_refresh = open_file()
        data_after['Applications'] = count - data_before_refresh['Applications']
        result1 = data_before_refresh['Appltype']
        result2 = dict(rows)
        data_after['Appltype'] = {key: result2.get(key, 0) - result1[key]  for key in result2}

        cur.execute("select count(*) from fda_staging.products")
        count = cur.fetchone()[0]
        print("Count=", count)
        data_before_refresh = open_file()
        data_after['Products'] = count - data_before_refresh['Products']

        cur.execute("select count(*) from fda_staging.submissions")
        count = cur.fetchone()[0]
        print("Count=", count)
        data_before_refresh = open_file()
        data_after['Submission'] = count - data_before_refresh['Submission']
        write_in_json(data_after)
        cur.close()

    except Exception as e:
        print("Exception issue-->",e)

    finally:
        if con is not None:
            con.close()

if (argv[1]=="before-refresh"):
    before_access_fda_report()
elif(argv[1]=="after-refresh"):
    after_access_fda_report()
else:
    print("Wrong choice")