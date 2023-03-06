from SivitasAkademik import SivitasAkademik

# deklarasi class


class Dosen(SivitasAkademik):

    # deklarasi private atribut
    __nip = ""
    __fakultas = ""
    __pend_terakhir = ""
    __keahlian = ""

    # constructor dengan parameter nip, nama

    def __init__(self, nip="", fakultas="", pend_terakhir="", keahlian="",):
        self.__nip = nip
        self.__fakultas = fakultas
        self.__pend_terakhir = pend_terakhir
        self.__keahlian = keahlian

    # setter dan getter untuk masing masing attribut nip, nama, fakultas, pend_terakhir, Keahlian
    def get_nip(self):
        return self.__nip

    def set_nip(self, nip):
        self.__nip = nip

    def get_fakultas(self):
        return self.__fakultas

    def set_fakultas(self, fakultas):
        self.__fakultas = fakultas

    def get_pend_terakhir(self):
        return self.__pend_terakhir

    def set_pend_terakhir(self, pend_terakhir):
        self.__pend_terakhir = pend_terakhir

    def get_keahlian(self):
        return self.__keahlian

    def set_keahlian(self, keahlian):
        self.__keahlian = keahlian
