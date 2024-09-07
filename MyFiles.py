import os
from MyDatabaseLib import MyDB

#primary root folder of all users. 
# whenever a new user will be signin. A seprate folder will be created for that user. 
# So each user will have his/her own folder in 'TRANSCODER_FOLDER'
MY_FOLDER = 'TRANSCODER_FOLDER'

SOURCE_DIR = 'Source'
DESTINATION_DIR = 'Destination'

class Files:
    # This function will create 'TRANSCODER_FOLDER' in working directory of project
    def create_folder():
        root_folder = os.path.join(os.getcwd(),MY_FOLDER)
        os.makedirs(root_folder, exist_ok=True)

    # This function will return the absolute path of 'TRANSCODER_FOLDER' folder
    def get_working_folder():
        root_folder = os.path.join(os.getcwd(),MY_FOLDER)
        return root_folder
    
    # This function will return the source folder path of the active user to save the uploaded files
    def get_source_file_path(email_address,file_name):
        
        file_name2 = os.path.join(os.getcwd(),MY_FOLDER, MyDB.get_user_folder(email_address), SOURCE_DIR, file_name)
        return file_name2

    # This function will return the destination folder path of the active user to save the transcoded files files
    def get_destination_file_path(email_address,file_name):
        file_name2 = os.path.join(os.getcwd(),MY_FOLDER, MyDB.get_user_folder(email_address), DESTINATION_DIR, file_name)
        return file_name2


