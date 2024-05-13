from connect import *

def updateFilm():
    
    try:
        idfield = int(input("Enter the ID of the film that you want to update: "))
        fieldName = input("Enter the field that you want to update: ") # This is column that user wants to update
        newValue =  input(f"Enter the value for {fieldName}: ")

        cursor.execute(f"UPDATE tblfilms SET {fieldName} = ? WHERE filmID = ?", (newValue, idfield))
        conn.commit() # This is the actual run the code soas to make the permanent change
        print(f"Film with this ID has now been updated {idfield}")
    

    except (sql.OperationalError, ValueError) as e:
        conn.rollback() # sends the code back to where the function was called
        print(f"Record not updated: {e}")


if __name__ == "__main__": # code is executed if this file is run2


    updateFilm()