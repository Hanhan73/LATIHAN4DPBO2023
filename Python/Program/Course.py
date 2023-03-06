# deklarasi class
class Course:

    # deklarasi private atribut
    __nama_matakuliah = ""

    # constructor dengan parameter nama_matakuliah

    def __init__(self, nama_matakuliah=""):
        self.__nama_matakuliah = nama_matakuliah

    # setter dan getter untuk masing masing attribut nama_matakuliah
    def get_nama_matakuliah(self):
        return self.__nama_matakuliah

    def set_nama_matakuliah(self, nama_matakuliah):
        self.__nama_matakuliah = nama_matakuliah
