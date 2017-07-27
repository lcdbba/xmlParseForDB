import cx_Oracle
from Modules import confParse
#dbTypeArr = {'oracle':'cx_Oracle','':'','':''}
class dbConnection():
    def __init__(self, dbType="oracle"):
        self.loginForm(dbType)
        self.conn = cx_Oracle.connect(self.fullUrl)
        self.getCursor()

    def loginForm(self, dbType="oracle"):
        conf = confParse("DBinfo.conf")
        info = conf.getSection("server")
        # self.dbType = info['db_type']
        self.host = info['host']
        self.user = info['user']
        self.passwd = info['password']
        self.port = info['port']
        self.database = info['schema']
        self.fullUrl = '{0}/{1}@{2}:{3}/{4}'.format(self.user, self.passwd, self.host, self.port, self.database)

    def exec_qry(self,query):
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return rows
        except cx_Oracle.DatabaseError:
            return None

    def exec_insert(self,query):
        try:
            self.cur.execute(query)
            return True
        except cx_Oracle.DatabaseError:
            return False

    def exec_insert_rows(self,query, rows):
        try:
            self.cur.executemany(query, rows)
            return True
        except cx_Oracle.DatabaseError:
            return False

    def getCursor(self):
        self.cur = self.conn.cursor()
        # return self.cur

    def __del__(self):
        self.cur.close()
        self.conn.close()
