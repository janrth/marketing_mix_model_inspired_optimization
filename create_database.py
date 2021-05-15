import numpy as np
import sqlite3


class database(object):
    '''
    Load csv, create database with columns and insert values from file
    '''
    def __init__(self, database_name, column_names, df):
        self.database_name = database_name
        self.column_names = column_names
        self.df = df

    def create_db(self):
        '''
        Make DB
        '''
        conn = sqlite3.connect(str(self.database_name)+'.db')
        conn.execute('DROP TABLE IF EXISTS {}'.format(self.database_name))
        c = conn.cursor()

        # Here I create only one column manually,
        # before adding multiple other columns in loop
        c.execute('''CREATE TABLE {} ({} REAL)'''.format(self.database_name,
                                                         self.column_names[0]))

        # Create all columns in loop
        col_names = self.column_names[1:]
        for column_name in col_names:
            '''This adds multiply columns to the database'''
            c.execute('''ALTER TABLE {} ADD COLUMN {} REAL'''.format(
                      self.database_name, column_name))

        # Insert all data in loop
        col_array = np.array(self.df[1:])

        for element in col_array:
            '''
            Now I insert into all columns
            '''
            placeholders = ', '.join(['?'] * self.df.shape[1])
            c.execute('''INSERT INTO {} VALUES ({})'''.format(
                self.database_name, placeholders), element)
        conn.commit()
