import sqlite3

class Database:
    def __init__(self, archive_name = "UsersDB.db"):
        self.conn = sqlite3.connect(archive_name)
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute("""
        create table if not exists users(
        id integer primary key autoincrement,
        name text not null,
        mail text not null
        )
        """)
        
        self.conn.commit()
        
    def insert_user(self, name, mail):
        self.cursor.execute(
            """
            insert into users(name, mail)
            values (?,?)
            """,
            (name, mail)
        )
        self.conn.commit()
        
    def list_users(self):
        self.cursor.execute(
            """
            select * from users
            """
            )
        return  self.cursor.fetchall()
    
    def clear_users(self):
        self.cursor.execute(
            """
            delete from users
            """
        )
        self.conn.commit()