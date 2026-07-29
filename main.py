from Libro import Libro
from Biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:

    print("\n===== BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Editar libro")
    print("5. Eliminar libro")
    print("6. Cantidad de libros")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año: "))

        libro = Libro(titulo, autor, anio)

        biblioteca.agregar_libro(libro)

    elif opcion == "2":

        biblioteca.mostrar_libros()

    elif opcion == "3":

        titulo = input("Ingrese el título del libro: ")

        biblioteca.buscar_libro(titulo)
    
    elif opcion == "4":
    
        titulo = input("Ingrese el título del libro a editar: ")

        biblioteca.editar_libro(titulo)

    elif opcion == "5":

        titulo = input("Ingrese el título del libro a eliminar: ")

        biblioteca.eliminar_libro(titulo)

    elif opcion == "6":
    
        biblioteca.cantidad_libros()
    
    elif opcion == "7":

        print("Hasta luego.")
        break

    else:

        print("Opción no válida.")