from SivitasAkademik import SivitasAkademik

# deklarasi class


class Mahasiswa(SivitasAkademik):

    # deklarasi private atribut
    __nim = ""
    __fakultas = ""

    # constructor dengan parameter nim, nama, prodi, dan fakultas
    def __init__(self, nim="", fakultas=""):
        self.__nim = nim
        self.__fakultas = fakultas

    # setter dan getter untuk masing masing attribut nim, nama, prodi dan fakultas
    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_fakultas(self):
        return self.__fakultas

    def set_fakultas(self, fakultas):
        self.__fakultas = fakultas
