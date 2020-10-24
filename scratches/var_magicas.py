def media(*args):
    return sum(args) / len(args)


def func(**kwargs):
    for nome, notas in kwargs.items():
        print("\n=====================================\n")
        print(f"nome do aluno   = {nome}")
        print(f"Notas do aluno  = {notas}")
        print(f"Media do aluno  = {media(*notas)}")


alunos = {
    "Joel":     [5, 7, 10],
    "Gil":      [3, 8, 10],
    "Paulo":    [10, 7, 9],
    "Artur":    [4, 9, 6]
}


func(**alunos)
