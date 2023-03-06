# deklarasi class
class Human:

    # deklarasi private atribut
    __nik = ""
    __nama = ""
    __jenis_kelamin = ""

    # constructor dengan parameter nik, nama, jenis_kelamin

    def __init__(self, nik="", nama="", jenis_kelamin=""):
        self.__nik = nik
        self.__nama = nama
        self.__jenis_kelamin = jenis_kelamin

    # setter dan getter untuk masing masing attribut nik, nama, jenis_kelamin
    def get_nik(self):
        return self.__nik

    def set_nik(self, nik):
        self.__nik = nik

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_jenis_kelamin(self):
        return self.__jenis_kelamin

    def set_jenis_kelamin(self, jenis_kelamin):
        self.__jenis_kelamin = jenis_kelamin
