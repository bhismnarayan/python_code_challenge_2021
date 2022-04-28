import database

def allshow():
    try:
        con=database.getDbConnection()
    # Create a cursor to perform database operations
        cursor = con.cursor()
       
    # Executing a SQL query
        cursor.execute("SELECT * from tvshow;")
    # Fetch result
        record = cursor.fetchall()
        return record
    except:
        return "Error occured"
    finally:
        if (con):
            cursor.close()
        con.close()
    return record

def getSpecificShow(id):
    con=database.getDbConnection()
    # Create a cursor to perform database operations
    cursor = con.cursor()
       
    # Executing a SQL query
    cursor.execute("SELECT * from tvshow where TVShowID='"+id+"';")
    # Fetch result
    record = cursor.fetchall()
    if (con):
        cursor.close()
        con.close()
    return record