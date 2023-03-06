from Course import Course

# deklarasi class


class ProgramStudi:

    # deklarasi private atribut
    __nama_prodi = ""
    __kode = ""
    __course = []

    # constructor dengan parameter nama_prodi, kode

    def __init__(self, nama_prodi="", kode=""):
        self.__nama_prodi = nama_prodi
        self.__kode = kode
        self.__course = []

    # setter dan getter untuk masing masing attribut nama_prodi, course
    def get_nama_prodi(self):
        return self.__nama_prodi

    def set_nama_prodi(self, nama_prodi):
        self.__nama_prodi = nama_prodi

    def get_kode(self):
        return self.__kode

    def set_kode(self, kode):
        self.__kode = kode

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course.append(course)
