class Libro:

    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio


    def convertir_diccionario(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio
        }


    def mostrar_info(self):
        print("----------------------")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año:", self.anio)