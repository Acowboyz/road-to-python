from MySQLdb import *

try:
    conn=connect(host="localhost", port=3306, user="root", passwd="", db="python3", charset="utf8", unix_socket="/var/run/mysqld/mysqld.sock")
    cursors1 = conn.cursor()

    sql = 'select * from students'
    cursors1.execute(sql)
    #result = cursors1.fetchone()
    result = cursors1.fetchall()
    print(result)
    conn.commit()
    cursors1.close()
    conn.close()
except Exception as e:
    raise Exception(str(e))
