from sqlencapsulation import Mysqlencap

# update
name = input("please enter the student's name:")
id1 = int(input("please enter the student's id:"))

sql = 'update students set name=%s where id=%s'
params=[name, id1]

sqlencap = Mysqlencap('localhost', 3306, 'python3', 'root', '')
sqlencap.create_update_delete(sql, params)

# search
sql = 'select id,name from students where id<5'
sqlencap = Mysqlencap('localhost', 3306, 'python3', 'root', '')
print(sqlencap.search(sql))
