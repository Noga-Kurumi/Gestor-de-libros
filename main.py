import function as fn
import os

def main():
    while True:
        try:
            option = int(input('''¡Bienvenido al gestor de libros!
                        \n1. Agregar libro
                        \n2. Eliminar libro
                        \n3. Buscar libro
                        \n4. Modificar libro
                        \n5. Mostrar libros
                        \n6. Guardar libros en un archivo CSV
                        \n7. Generar grafico de libros por año
                        \n8. Salir
                        \n\nPor favor, seleccione una opcion: '''))
            if option == 1:
                os.system("cls")
                while True:
                    print(" - AGREGAR LIBRO -\n")
                    title = input("Por favor introduzca el nombre del libro: ")
                    author = input("Por favor introduzca el autor del libro: ")
                    genre = input("Por favor introduzca el genero del libro: ")
                    try:
                        year = int(input("Por favor introduzca el año del libro: "))
                        fn.addBook(title,author,genre,year)
                        os.system("cls")
                        print("Libro añadido!\n")
                        break
                    except:
                        os.system("cls")
                        print("Debe ingresar un año valido!\n")

            elif option == 2:
                os.system("cls")
                books = fn.getBooks()
                if len(books) > 0:
                    while True:
                        print(" - ELIMINAR LIBRO -\n")
                        fn.showBooks()
                        try:
                            n = int(input("\nPor favor, seleccione un libro para eliminar: "))
                            fn.deleteBook(n)
                            break
                        except:
                            os.system("cls")
                            print("Debe ingresar un numero valido!\n")
                else:
                    fn.noBooks()

            elif option == 3:
                os.system("cls")
                books = fn.getBooks()
                if len(books) > 0:
                    print(" - BUSCAR LIBRO -\n")
                    title = input("Por favor, ingrese el titulo del libro: ")
                    found, book = fn.searchBook(title)
                    if found == True:
                        for i, v in book.items():
                            print(f"{i}: {v}\n")
                        print("---------------------------------------\n")
                    else:
                        os.system("cls")
                        print("Libro no encontrado!\n")
                else:
                    fn.noBooks()
            
            elif option == 4:
                os.system("cls")
                books = fn.getBooks()
                if len(books) > 0:
                    print(" - MODIFICAR LIBRO -\n")
                    fn.showBooks()
                    i = int(input("\nSeleccione un libro para modificar: "))
                    c = input("Seleccione el campo a editar | Title | Author | Genre | Year | : ")
                    n = input("Ingrese el nuevo valor del campo: ")
                    fn.modifyBook(i,c,n)              
                else:
                    fn.noBooks()

            elif option == 5:
                os.system("cls")
                books = fn.getBooks()
                if len(books) > 0:
                    print("- LIBROS ENCONTRADOS -\n")
                    fn.showBooks()
                    print("---------------------------------------\n")
                else:
                    fn.noBooks()

            elif option == 6:
                books = fn.getBooks()
                if len(books) > 0:
                    os.system("cls")
                    fn.createCSV()
                else:
                    fn.noBooks()
            
            elif option == 7:
                books = fn.getBooks()
                if len(books) > 0:
                    fn.createGraphic()
                    os.system("cls")
                else:
                    fn.noBooks

            elif option == 8:
                os.system("cls")
                print("Saliendo...")
                break
            else:
                os.system("cls")
                print("Por favor, selecciona una opcion valida!\n")
        except:
            os.system("cls")
            print("Por favor, selecciona una opcion valida!\n")

if __name__ == "__main__":
    main()