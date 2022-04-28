from flask import  Flask
import psycopg2
from psycopg2 import Error
import middletier

app=Flask(__name__)

@app.route("/tvshow/",methods=['GET'])
def getallepisode():
    return {'show':middletier.allshow()}

@app.route('/tvshow/<string:id>/',methods=['GET'])
def getSpecificEpisode(id):
    return {'showDetails':middletier.getSpecificShow(id)}



@app.route("/")
def hello_world():
    connection=""
    try:
    # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                  password="Mango123$",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT * from tvshow;")
        # Fetch result
        record = cursor.fetchall()
        #print("You are connected to - ", record, "\n")
        for i in record:
            print(i)

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return "Hello Worlds"