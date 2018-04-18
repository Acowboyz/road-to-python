from MySQLdb import *

class Mysqlencap(object):
    def __init__(self, host, port, db, user, passwd, charset='utf8', sock='/var/run/mysqld/mysqld.sock'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.sock = sock

    def open(self):
        self.conn = connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset, unix_socket=self.sock)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def create_update_delete(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            raise Exception(str(e))

    def search(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()

            return result
        except Exception as e:
            raise Exception(str(e))


