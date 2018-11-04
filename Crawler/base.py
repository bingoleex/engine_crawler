import sqlite

FILE_NAME = 'result.db'

class Base(object):

    def execute(self, sql):
        with sqlite3.connect(FILE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(exe_sql)
            conn.commit() 

    def select(self, sql):
        with sqlite3.connect(FILE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(exe_sql)
            data = cursor.fetchall()

        return  data

    def execute_many(self, sqls):
        with sqlite3.connect(FILE_NAME) as conn:
            cursor = conn.cursor()
            for sql in sqls:
                cursor.execute(exe_sql)

            conn.commit()