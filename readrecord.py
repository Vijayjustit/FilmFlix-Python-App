"Objectives"
"" '' # Import connect module
"" '' # Create a function to read record(s) from a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	



from connect import * # import everything from the connect.py file

def readRecords():
    
    try:
        cursor.execute(f"SELECT * FROM tblfilms") # selects all the records from the tblfilms table
        row = cursor.fetchall() # obtain all the recods and they are stored in the row variable

        for aRecord in row:
            print(aRecord)
            
    except sql.OperationalError as e:
        print(f"Records not found: {e}")

if __name__ == "__main__":
    
    readRecords()