# INSERT QUERY function

import creds
import mariadb

def connect_db():
    conn=None
    cursor=None

    try:
        conn = mariadb.connect(
                                user=creds.user,
                                password=creds.password,
                                host=creds.host,
                                port=creds.port,
                                database=creds.database
                                )

        cursor = conn.cursor()
        return (conn, cursor)
    except mariadb.OperationalError as e:
        print("Got an operational Error")
        if("Access denied" in e.msg):
            print("Failed to Connect to DataBase")
        disconnect_db()

def disconnect_db(conn, cursor):
    if(cursor != None):
        cursor.close()
    if(conn != None):
        conn.rollback()
        conn.close()
        
def run_query(statement, args=None):
    
    try:
        (conn, cursor) = connect_db()
        if statement.startswith("SELECT username, content from blog_post"):
            cursor.execute(statement, args)
            result = cursor.fetchall()
            
            print("Total of {} Comments".format(cursor.rowcount))
            return result
        elif statement.startswith("SELECT username, password FROM user WHERE username=? and password=?"):
            cursor.execute(statement, args)
            result = cursor.fetchall()
            if cursor.rowcount ==1:
                print("Total of {} users".format(cursor.rowcount))
                return result
            else:
                exit()
        else:
            cursor.execute(statement, args)
            if cursor.rowcount == 1:
                conn.commit()
                print("Query successful")
            else:
                print("Query to insert")
    
    except mariadb.OperationalError as e:
        print("Got an operational Error")
        if("Access denied" in e.msg):
            print("Failed to Log-in")
        print(e.msg)
    
    except mariadb.IntegrityError as e:
        if("CONSTRAINT `users_CHECK_age`" in e.msg):
            print("User is outside of acceptable age range")
        elif("Duplicate entry" in e.msg):
            print("User already exists")
        else:
            print(e.msg)

    except mariadb.ProgrammingError as e:
        if("SQL syntax" in e.msg):
            print("Apparently you cannot program")
        else:
            print("Got a different programming error")
        print(e.msg)
    
    except RuntimeError as e:
        print("Caught a runtime error")
        e.__traceback__

    except Exception as e:
        print(e.with_traceback)

        print(e.msg)
    finally:
        disconnect_db(conn,cursor)


