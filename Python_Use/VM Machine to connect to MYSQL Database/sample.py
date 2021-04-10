#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Connect to remote mysql database through springboard
author: gxcuizy
time: 2018-08-10
"""

import pymysql
from sshtunnel import SSHTunnelForwarder

# Program main entrance
if __name__ == "__main__":
    # Springboard SSH connection
    with SSHTunnelForwarder(
            ('192.168.0.1', 22),
            ssh_username="test",
            ssh_pkey="test.pem",
            remote_bind_address=('*************mysql.rds.aliyuncs.com', 3306)
    ) as a  tunnel :
        # Database connection configuration, host defaults to 127.0.0.1 without modification
        conn = pymysql.connect(
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            user='root',
            password='root',
            db='test',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        # Get the cursor
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # Query the database, query a piece of data, other CURD operations are similar
        sql = "SELECT name FROM table_name WHERE id = '%s'"
        prams = ('1',)
        cursor.execute(sql % prams)
        info = cursor.fetchone()
        print(info)
        # Close connection
        cursor.close()
        conn.close()
