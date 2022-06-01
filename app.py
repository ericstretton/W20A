import creds
import mariadb
from helpers.welcome import welcome

conn = mariadb.connect(
                        user=creds.user,
                        password=creds.password,
                        host=creds.host,
                        port=creds.port,
                        database=creds.database
                        )

cursor = conn.cursor()

welcome()
username = input("Username: ")

def blog_interface_loop():
    pass
# Two choices
#Choice number one is to make a new post (insert query)
#Choice number two is to view all posts (select query)
