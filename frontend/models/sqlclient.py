import psycopg2
import pandas as pd
from pandas import DataFrame
from pandas import *
from sqlalchemy import create_engine
import json

class SqlClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 5432
        self.user = 'testuser'
        self.password = 'password'
        self.connect_timeout = 30
        self.sslmode = 'require'
        self.dbname = 'postgres'
        try:
            self.connection = psycopg2.connect(host=self.host,
                                               port=self.port,
                                               user=self.user,
                                               password=self.password,
                                               database=self.dbname,
                                               connect_timeout=self.connect_timeout);
            self.cursor = self.connection.cursor()
            
            self.engine_string = "postgresql+psycopg2://%s:%s@%s:%d/%s" % (self.user, self.password, self.host, self.port, self.dbname)
            self.engine = create_engine(self.engine_string)

            print('Successfully connected to redshift')
            return
        except psycopg2.Error as err:
            print("Error in getting login Info sqlclient inti")
            return err


    def getLogin(self,email,passd):
        try:
            sql = "SELECT name,email,phone,location FROM users WHERE email='"+email+"' AND password='"+passd+"'"
            df = pd.read_sql_query(sql,con=self.engine)
            if (df.empty):
                print("Empty dataframe in getSomething")
                self.connection.close()
                exit(1)
            self.connection.close()
            return df
        except psycopg2.Error as err:
            print("Error in getting login Info getLogin")
            return err