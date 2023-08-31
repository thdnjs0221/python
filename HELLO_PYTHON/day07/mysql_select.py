import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')

cur=conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from emp"

cur.execute(sql)
result = cur.fetchall()

for data in result :
    print(data)

conn.close()

