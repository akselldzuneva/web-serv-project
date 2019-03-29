import sqlite3

class DB:
    def __init__(self):
        conn = sqlite3.connect('activ.db', check_same_thread=False)
        self.conn = conn
     
    def get_connection(self):
        return self.conn
     
    def __del__(self):
        self.conn.close()
        
    def insert(self, username, info, about, whatelse, sphere):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO aktiv 
                          (user_name, ur_info, about_u, what_else, acceptt, spheree) 
                          VALUES (?,?,?,?,?)''', (username, info, about, whatelse,  sphere))
        cursor.close()
        self.connection.commit()    
        
    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row
     
    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows    
    