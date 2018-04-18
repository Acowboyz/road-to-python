from sqlencapsulation import Mysqlencap
from hashlib import sha1

# receive the user login information
name = input("please enter the user's name:")
pwd = input("please enter the user's password:")

# encrypt the password
s1 = sha1()
s1.update(pwd.encode("utf-8"))
pwd2 = s1.hexdigest()
print(pwd2)

sql = "select passwd from users where name=%s"
sqlencap = Mysqlencap('localhost', 3306, 'python3', 'root', '')
result = sqlencap.search(sql,[name])

if len(result) == 0:
    print("error user's name !")
elif result[0][0] == pwd2:
    print("login success !")
else:
    print("error password !")

