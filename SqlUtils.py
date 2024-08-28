import csv, re, sys, os
import sqlite3

class SqlUtils():
    """Utility class to work with SQLite3 databases in Python"""
    def __init__(self,sqlfile):
        """Initialize the current object with the sqlite3 database filename
        
        Args:
            sqlfile (str): filename of a sqlite3 file, must not exists
        """
        pass
    def csv2sql (self,csvfile, tablename,delimiter=',',quotechar='"'):
        """Importing a Csv or Tab file into a SQLite3 database.
        
        Args:
            csvfile (str): filename of a csv or tabfile, must exists
            tablename (str): the table name into which to import the data
            delimiter (chr): character which separates the columns in the csv file, defaults to ','
            quotechar (chr): quoting character, defaults to the double quote
        Return:
            int : number of rows added from the csvfile
        """
        # Code outline:
        #   create sql connection
        #   open csv file
        #   create reader
        #   loop over file
        #   first line create column names create table 
        #   next lines insert data into table
        #   close all connections (database, csv reader, file)
        #   return number of inserted rows
        pass
    def getTables (self):
        """Return the table names of the database.
        
        Returns:
            list : names of tables
        """
        pass

def help(argv):
    usage()
    print(__doc__)

def usage(argv):
    print(f"Usgae: {(argv[0])} csvfile sqllite3file ?(tablename)")

def main(argv):
    if "--help" in argv:
        help(argv)
    elif len(argv)<3:
        usage(argv)
        exit()
    elif not (os.path.exists(argv[1]):
        print (f"Error: file {argv[1]} doesn't exist:")
    else:
        tablename=re.sub("[^A-Za-z0-9_]","",argv[1])
        sqlfile=argv[2]
        tabfile=argv[1]
        if (len(argv)==4):
            tablename=argv[3]
        sql=SqlUtils
        print("All Line")
    # check length of arguments 
    # should be app-csv2sqlite csvfile sqlitefile
    # check if csv file exists
    # if exists create object
    # call csv2sqlite3

if __name__ == '__main__':
    main(sys.argv)
