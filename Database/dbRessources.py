# -*- coding: Utf-8 -*
import mysql.connector
from os import system
import os
from mysql.connector import errorcode
from Database.Params.params import params
from Database.Params.file_path import path


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(**params)
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR or err.errno == errorcode.ER_BAD_DB_ERROR:
            return err.errno
        else:
            print(err)
    else:
        conn.close()


def create_database():
    command0 = """ mysql -u %s -p%s --host %s --port %s  -e "create database  %s; use %s;" """ %(params['user'], params['password'], params['host'], params['port'],params['database'],params['database'])
    system(command0)
    command1 = """mysql -u %s -p%s --host %s --port %s  < %s""" %(params['user'], params['password'], params['host'], params['port'],'Database//Script//'+ path['file'])
    system(command1)  
