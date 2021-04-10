# -*- coding: utf-8 -*-

from os import path
import sqlite3

DB_PATH = path.abspath(path.join(path.dirname(__file__), '../../data/main.db'))
IS_LOG = True


class Context():
    _error = False

    def __enter__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        return self

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.cursor

    def is_error(self):
        return self._error

    def exec(self, sqlstr, args=None):
        ''' 只负责执行sql语句, 返回是否执行成功 '''
        try:
            if args:
                self.cursor.execute(sqlstr, args)
            else:
                self.cursor.execute(sqlstr)
        except Exception as e:
            if IS_LOG:
                print("DBContext Error: ", e)
            self._error = True
            return False
        return True

    def execmany(self, sqlstr, vals):
        try:
            self.conn.executemany(sqlstr, vals)
        except Exception as e:
            if IS_LOG:
                print("DBContext Error: ", e)
            self._error = True
            return False
        return True

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self._error = True
        else:
            self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    print(DB_PATH)
    print(path.abspath(path.dirname(__file__)))
    print(path.abspath(path.join(path.dirname(__file__), '../../data/main.db')))
