import pymysql
from dotenv import load_dotenv
import os
from sshtunnel import SSHTunnelForwarder



def get_connection():
    load_dotenv()
    MYSQL_SERVER = os.getenv('MYSQL_SERVER')
    MYSQL_PORT = os.getenv('MYSQL_PORT')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    SSH_SERVER = os.getenv('SSH_SERVER')
    SSH_PORT = int(os.getenv('SSH_PORT'))
    SSH_USER = os.getenv('SSH_USER')
    SSH_PASSWORD = os.getenv('SSH_PASSWORD')

    tunnel = SSHTunnelForwarder((SSH_SERVER, SSH_PORT), ssh_password=SSH_PASSWORD, ssh_username=SSH_USER,
                                remote_bind_address=(MYSQL_SERVER, 3306))
    tunnel.start()

    connection = pymysql.connect(
        host=MYSQL_SERVER,
        port=tunnel.local_bind_port,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection