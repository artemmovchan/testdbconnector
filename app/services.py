from models import DBConnector

def send_sql_query_service(data):
    host = data.get('host')
    dbname = data.get('dbname')
    driver = data.get('driver')
    function = data.get('function')
    username = data.get('username')
    password = data.get('password')
    if (host is not None and dbname is not None and driver is not None and function is not None and username is not None and password is not None):
        return DBConnector(driver=driver,
                             host=host,
                             dbname=dbname,
                             username=username,
                             password=password).send_sql_query(function=function)
    else:
        raise Exception('Missing parameters')