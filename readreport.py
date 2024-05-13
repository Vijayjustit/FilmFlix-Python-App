from connect import * # import everything from the connect.py file

def genre():
    genre = input("Please enter a genre: ").title()
    try:
        cursor.execute(f"SELECT * FROM tblfilms WHERE genre = '{genre}'") # selects all the records from the songs table
        row = cursor.fetchall() # obtain all the recods and they are stored in the row variable
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")

def year():
    year = int(input("Please enter the year released: "))
    try:
        cursor.execute(f"SELECT * FROM tblfilms WHERE year = '{year}'") # selects all the records from the songs table
        row = cursor.fetchall() # obtain all the recods and they are stored in the row variable
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")

    

def rating():
    rating = input("Please enter the rating: ")
    try:
        cursor.execute(f"SELECT * FROM tblfilms WHERE rating = '{rating}'") # selects all the records from the songs table
        row = cursor.fetchall() # obtain all the recods and they are stored in the row variable
        for aRecord in row:
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")

if __name__ == "__main__":
    
    genre()
    year()
    rating()