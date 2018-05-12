from redistest import redisHelper
from sqlencapsulation import Mysqlencap
from hashlib import sha1

# receive data input

name = input("please input the name:")
pwd = input("please input the password:")

# hasing
s1 = sha1()
s1.update(pwd.encode('utf-8'))
pwd_h = s1.hexdigest()

# search redis
r = redisHelper('localhost', 6379)
m = Mysqlencap('localhost', 3306, 'python3', 'root', '')

if r.get(name) == None:
    print('search from mysql')
    sql = 'select passwd from users where name=%s'
    pwd_mysql = m.searchone(sql, [name])
    if pwd_mysql == None:
        print('user name error')
    # elif pwd_mysql[0] == pwd_h:
    #     print('success')
    # else:
    #     print('password error')
    else:
        # search the data from mysql and save to the redis server
        r.set(name, pwd_mysql[0])
        if pwd_mysql[0] == pwd_h:
            print('success')
        else:
            print('password error')
else:
    print('search from redis')
    if r.get(name).decode('utf-8') == pwd_h:
        print('success')
    else:
        print('password error')




