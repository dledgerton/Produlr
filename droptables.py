#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute('DROP TABLE COMPANY')

print("Table dropped successfully");

conn.close()

