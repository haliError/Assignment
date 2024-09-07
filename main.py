from VideoTranscoding import create_app
from MyDatabaseLib import MyDB
#from MyFiles import Files



if __name__ == '__main__':

    app = create_app()
    app.run(debug = True)


