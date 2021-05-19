""" __author__: Leynilson José "Snake" """
# Telefone sem fio | por enviar

import os
import sys
from io import BytesIO, IOBase


def countSemelhancas(frase1: str, frase2: str, fraseOriginal: str):
    semelhancas = [0, 0]
    for letra1, letra2, letraOriginal in zip(frase1, frase2, fraseOriginal):
        if letra1 == letraOriginal:
            semelhancas[0] += 1
        if letra2 == letraOriginal:
            semelhancas[1] += 1
    return semelhancas


def desfazerEmpate(frase1: str, frase2: str, fraseOriginal: str):
    for letra1, letra2, letraOriginal in zip(frase1, frase2, fraseOriginal):
        if letra1 == letraOriginal and letra2 != letraOriginal:
            return 1
        elif letra1 != letraOriginal and letra2 == letraOriginal:
            return 2
    return 0


def main():
    k = 0
    t = int(input())
    while t > 0:
        t -= 1
        k += 1
        original = input()
        team1 = input()
        team2 = input()
        print('Instancia', k)
        p1, p2 = countSemelhancas(team1, team2, original)
        if p1 > p2:
            print('time 1')
        elif p2 > p1:
            print('time 2')
        else:
            decisiao_final = desfazerEmpate(team1, team2, original)
            if decisiao_final == 0:
                print('empate')
            else:
                print('time', decisiao_final)
        print()


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")

# endregion


if __name__ == "__main__":
    main()
