class Tempo:
    """ Classe com metodos para converter unidades de tempo;\n
        Segundos, Minutos, Horas e Dias
    """

    def __init__(self, tmp, formato="s"):
        if formato in "smhd":
            self.formato = formato.lower()
            self.tmp = tmp
        else:
            raise NameError(
                "Valor inválido! Escolha:\n(s) segundos\n(m) minutos\n(h) horas\n(d) dias"
                )

    def __str__(self):
        return self.info()

    def __repr__(self):
        return self.info()

    def __lt__(self, other):
        return self.em_sec() < other.em_sec()

    def __le__(self, other):
        return self.em_sec() <= other.em_sec()

    def __gt__(self, other):
        return self.em_sec() > other.em_sec()

    def __ge__(self, other):
        return self.em_sec() >= other.em_sec()

    def __eq__(self, other):
        return self.em_sec() == other.em_sec()

    def __ne__(self, other):
        return self.em_sec() != other.em_sec()

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Tempo(self.tmp + other, self.formato)
        if isinstance(other, Tempo):
            if self.formato == other.formato:
                return Tempo(self.tmp + other.tmp, self.formato)
            return Tempo(self.em_sec() + other.em_sec())

        raise ArithmeticError(
            "Operação Inválida! Verifique se os valores são instancias de 'int', 'float' ou 'Tempo'"
        )

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Tempo(self.tmp - other, self.formato)
        if isinstance(other, Tempo):
            if self.formato == other.formato:
                return Tempo(self.tmp - other.tmp, self.formato)
            return Tempo(self.em_sec() - other.em_sec())

        raise ArithmeticError(
            "Operação Inválida! Verifique se os valores são instancias de 'int', 'float' ou 'Tempo'"
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Tempo(self.tmp * other, self.formato)
        if isinstance(other, Tempo):
            if self.formato == other.formato:
                return Tempo(self.tmp * other.tmp, self.formato)
            return Tempo(self.em_sec() * other.em_sec())

        raise ArithmeticError(
            "Operação Inválida! Verifique se os valores são instancias de 'int', 'float' ou 'Tempo'"
        )

    def __div__(self, other):
        if isinstance(other, (int, float)):
            return Tempo(self.tmp / other, self.formato)
        if isinstance(other, Tempo):
            if self.formato == other.formato:
                return Tempo(self.tmp / other.tmp, self.formato)
            return Tempo(self.em_sec() / other.em_sec())

        raise ArithmeticError(
            "Operação Inválida! Verifique se os valores são instancias de 'int', 'float' ou 'Tempo'"
        )


    def em_sec(self):
        """Converte para segundos"""
        if self.formato == "m":
            self.tmp *= 60
        elif self.formato == "h":
            self.tmp *= 3600
        elif self.formato == "d":
            self.tmp *= 86400
        self.formato = "s"
        return self.tmp

    def em_min(self):
        """Converte para minutos"""
        if self.formato == "s":
            self.tmp /= 60
        elif self.formato == "h":
            self.tmp *= 60
        elif self.formato == "d":
            self.tmp *= 1440
        self.formato = "m"
        return self.tmp

    def em_hora(self):
        """Converte para horas"""
        if self.formato == "s":
            self.tmp /= 3600
        elif self.formato == "m":
            self.tmp /= 60
        elif self.formato == "d":
            self.tmp *= 24
        self.formato = "h"
        return self.tmp

    def em_dia(self):
        """Converte para dias"""
        if self.formato == "s":
            self.tmp /= 86400
        elif self.formato == "m":
            self.tmp /= 1440
        elif self.formato == "h":
            self.tmp /= 24
        self.formato = "d"
        return self.tmp

    def info(self):
        """ Mostra estado actual do objecto """
        out = f"sec: {self.em_sec()}\nmin: {self.em_min()}"
        out += f"\nhora: {self.em_hora()}\ndia: {self.em_dia()}"
        return out



# print("\nSec / Min:   ", Tempo(120, "s").em_min())
# print("Sec / Hora:  ", Tempo(3600, "s").em_hora())
# print("Min / Sec:   ", Tempo(2, "m").em_sec())
# print("Min / Hora:  ", Tempo(60, "m").em_hora())
# print("Hora / Sec:  ", Tempo(2, "h").em_sec())
# print("Hora / Min:  ", Tempo(2, "h").em_min())
# print("Sec / Dia:  ", Tempo(24, "f").em_dia(), "\n")

print(Tempo(48, "h") + Tempo(24, "h"), end="\n\n")
print(Tempo(3, "d") - Tempo(1, "h"))
# t = Tempo(72, "h")
# print(isinstance(t, Tempo))
