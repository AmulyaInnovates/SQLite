# -*- coding: utf-8 -*-
"""Intro.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17_DdQxC5FdWieZD_cum8iE_9zzpLxfRI
"""

from google.colab import files
file= files.upload()

import sqlite3

database= "database.sqlite"
conn= sqlite3.connect(database)
print("Opened the data successfully")

import pandas as pd
tables= pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
tables

tables_2= pd.read_sql("""SELECT * FROM Player""",conn)
tables_2