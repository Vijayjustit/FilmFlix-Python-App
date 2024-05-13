from connect import *

def insertFilm():
  

    try:
          #Create an empty list
        film=[]

    #obtain values from the user
        title = input("Enter film title: ").title()
        yearReleased = int(input("Enter year released: "))
        rating = input("Enter the rating as PG or R or G: ").upper()
        duration = int(input("Enter the film duration: "))
        genre = input("Enter film Genre: ").title()



    #append data to the list "tblfilms"
        film.append(title)
        film.append(yearReleased)
        film.append(rating)
        film.append(duration)
        film.append(genre)

        # film = film + [title, yearReleased, rating, duration, genre]
        # print(films)
        cursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", film)
        conn.commit() # makes the permanent
        print(f"{title} added to the films table")

    except (sql.OperationalError, ValueError) as e:
        conn.rollback() # sends the code back to where the function was called
        print(f"Record not added: {e}")


if __name__ == "__main__": # code is executed if this file is run


    insertFilm()