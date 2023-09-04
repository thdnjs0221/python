import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

curs = conn.cursor()
sql = """insert into emp values (%s,%s,%s,%s)"""
curs.execute(sql,('3','3','3','3'))
curs.execute(sql,('4','4','4','4'))

conn.commit()

curs.close()
conn.close()
