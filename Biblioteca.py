import json
from Libro import Libro


class Biblioteca:

    def __init__(self):
        self.libros = []
        self.cargar_libros()


    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.guardar_libros()


    def guardar_libros(self):

        datos = []

        for Libro in self.libros:
            datos.append(Libro.convertir_diccionario())


        with open("libros.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)


    def cargar_libros(self):

        try:
            with open("libros.json", "r") as archivo:

                datos = json.load(archivo)#lee los datos


                for libro in datos:

                    nuevo_libro = Libro(
                        libro["titulo"],
                        libro["autor"],
                        libro["anio"]
                    )

                    self.libros.append(nuevo_libro)


        except FileNotFoundError:
            # Si el archivo no existe, empieza vacío
            pass



    def buscar_libro(self, texto):

        encontrados = []

        for libro in self.libros:

            if (texto.lower() in libro.titulo.lower() or 
                texto.lower() in libro.autor.lower()):

                encontrados.append(libro)
        
        for libro_encontrado in encontrados:
            libro_encontrado.mostrar_info()
  
       



    def mostrar_libros(self):

        if len(self.libros) == 0:
            print("No hay libros registrados")
            return


        for libro in self.libros:
            libro.mostrar_info()

    def editar_libro(self, titulo_buscar):

        for libro in self.libros:

            if libro.titulo.lower() == titulo_buscar.lower():

                print("Libro encontrado")

                nuevo_titulo = input("Nuevo título: ")
                nuevo_autor = input("Nuevo autor: ")
                nuevo_anio = input("Nuevo año: ")


                libro.titulo = nuevo_titulo
                libro.autor = nuevo_autor
                libro.anio = nuevo_anio


                self.guardar_libros()

                print("Libro actualizado correctamente")
                return


        print("No se encontró el libro")
    
    def eliminar_libro(self, titulo_buscar):

        for libro in self.libros:

            if libro.titulo.lower() == titulo_buscar.lower():

                self.libros.remove(libro)

                self.guardar_libros()

                print("Libro eliminado correctamente")
                return


        print("No se encontró el libro")


    def cantidad_libros(self):

        print(len(f"Cantidad total de libros : {self.libros}")) 