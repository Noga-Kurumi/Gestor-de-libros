import pandas as pd
import matplotlib.pyplot as plt
import os

books = [{"Title":"asd", "Author":"Tumama", "Genre":"asd", "Year":1982}]

def noBooks():
    print("No existen libros guardados, primero guarde al menos 1 libro.\n")

def addBook(title, author, genre, year):
    books.append({"Title":title, "Author":author, "Genre":genre, "Year":year})

def getBooks():
    return books

def deleteBook(n):
    try:
        del books[n]
        print("Libro eliminado!")
    except:
        os.system("cls")
        print("No se pudo eliminar el libro! El libro no existe.\n")

def searchBook(title):
    for book in books:
        if book["Title"] == title:
            os.system("cls")
            print("- LIBRO ENCONTRADO -\n")
            return True, book
    return False, book

def showBooks():
    for n, i in enumerate(books):
        print(f"{n}. {i["Title"]}, {i["Author"]}, {i["Genre"]}, {i["Year"]}.")

def modifyBook(book, field, newvalue):
    for n, i in enumerate(books):
        if n == book:
            toModify = i
            if field in toModify:
                toModify[field] = newvalue
                os.system("cls")
                print("Se modificó el libro correctamente!\n")
                return
            else:
                os.system("cls")
                print("El campo seleccionado no existe!\n")
                return
    os.system("cls")
    print("El libro seleccionado no existe!\n")

def createCSV():
    Titles = []
    Authors = []
    Genres = []
    Years = []
    for book in books:
        Titles.append(book["Title"])
        Authors.append(book["Author"])
        Genres.append(book["Genre"])
        Years.append(book["Year"])
    CSVdict = {"Title":Titles,"Author":Authors,"Genre":Genres,"Year":Years}
    df = pd.DataFrame(CSVdict)
    df.to_csv("Gestor De Libros\\RegistroDeLibros.csv")
    print("Se guardo un archivo CSV exitosamente!\n")

def createGraphic():
    years = [book["Year"] for book in books]
    unique_years = list(set(years))
    books_per_year = [years.count(year) for year in unique_years]

    plt.plot(unique_years, books_per_year)
    plt.show()