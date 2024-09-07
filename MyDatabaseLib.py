import sqlite3

MY_DATABASE = 'video_transcoder.db'

class MyDB:
    def create_db():
        with sqlite3.connect(MY_DATABASE) as conn:
            cursor = conn.cursor()
            #Crearte USERS table with two users
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                              email_address TEXT PRIMARY KEY ,
                              password TEXT NOT NULL,
                              private_directory TEXT NOT NULL
                              )''')
            cursor.execute('''Insert into users(email_address, password, private_directory) values 
                           ('mohsinlabs@yahoo.com','mali','A12345')''')
            cursor.execute('''Insert into users(email_address, password, private_directory) values 
                           ('hali.wahvillage@gmail.com','hali','B56789')''')
            conn.commit()
            #----------------------------------
            #Crearte FILES_INFO table 
            cursor.execute('''CREATE TABLE IF NOT EXISTS files_info (
                              Record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                              email_address TEXT ,
                              uploaded_file TEXT NOT NULL,
                              transconded_file TEXT NOT NULL
                              )''')
            conn.commit()

    def get_users_data():
        users_passwords = {}

        with sqlite3.connect(MY_DATABASE) as conn:
            cursor = conn.cursor()
            #extract USERS table
            cursor.execute('''select email_address, password from users order by email_address''')
            data = cursor.fetchall()
            for (u, p) in data:
                users_passwords[u] = p
        return users_passwords

    def get_users_files(email_address):
        files = {}

        with sqlite3.connect(MY_DATABASE) as conn:
            cursor = conn.cursor()
            #extract USERS passwords
            sql = ("select uploaded_file, transconded_file from files_info where email_address = '" +
                   email_address + "'" )

            cursor.execute(sql)
            files = cursor.fetchall()
        return files

    def get_user_folder(email_address):
        user_folder = ''

        with sqlite3.connect(MY_DATABASE) as conn:
            cursor = conn.cursor()
            #extract USER folder
            sql = ("select private_directory from users where email_address = '" +
                   email_address + "'" )

            cursor.execute(sql)
            folders = cursor.fetchall()
            user_folder = folders[0][0]
        return user_folder


    def update_users_files(email_address, s_file, d_file):

        with sqlite3.connect(MY_DATABASE) as conn:
            cursor = conn.cursor()
            #extract USERS table
            sql = ("insert into files_info(email_address, uploaded_file, transconded_file) values ('" + 
                   email_address + "', '" + s_file + "', '" + d_file + "')" )
            cursor.execute(sql)
#            sql = ("insert into files_info(email_address, uploaded_file, transconded_file) values ('mohsinlabs@yahoo.com', 'happy feet.mp4', 'happy feet.mp3')" )
#            cursor.execute(sql)
#            sql = ("insert into files_info(email_address, uploaded_file, transconded_file) values ('hali.wahvillage@gmail.com', 'my_movie.mp4', 'my_movie.wav')" )
#            cursor.execute(sql)
#            sql = ("insert into files_info(email_address, uploaded_file, transconded_file) values ('hali.wahvillage@gmail.com', 'hello.mp4', 'hello.mov')" )
#            cursor.execute(sql)

            conn.commit()

    