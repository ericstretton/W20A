import creds
import mariadb

conn = mariadb.connect(
                        user=creds.user,
                        password=creds.password,
                        host=creds.host,
                        port=creds.port,
                        database=creds.database
                        )

cursor = conn.cursor()