import sqlite3


class DBConnect:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("create instance")
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect("./test.db", check_same_thread=False)
            cls._instance._init = False
        return cls._instance

    def __init__(self):
        if self._init:
            return
        self.conn.row_factory = sqlite3.Row
        self._init = True
        print("init instance")

    def get_connect(self):
        return self.conn

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()