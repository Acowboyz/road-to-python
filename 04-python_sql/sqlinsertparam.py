from MySQLdb import *

try:
    name = input("please enter the student's name:")
    conn=connect(host="localhost", port=3306, user="root", passwd="", db="python3", charset="utf8", unix_socket="/var/run/mysqld/mysqld.sock")
    cursors1 = conn.cursor()

    sql = 'insert into students(name) value(%s)'
    cursors1.execute(sql, [name])
    conn.commit()
    cursors1.close()
    conn.close()
except Exception as e:
    raise Exception(str(e))
