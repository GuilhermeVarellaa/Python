import cx_Oracle
import json

def connect_to_database():
    with open("./db_oracle.json", "r") as file:
        db_variables = json.load(file)

    cx_Oracle.init_oracle_client(lib_dir=db_variables["oracle_client_path"])

    username = db_variables["username"]
    password = db_variables["password"]
    server = db_variables["server"]
    port = db_variables["port"]
    dbname = db_variables["dbname"]

    dsn = cx_Oracle.makedsn(server, port, dbname)
    conn = cx_Oracle.connect(username, password, dsn)
    return conn
