frase = str(input('Degite uma frase ')).upper().strip()
print('A letra A aparece {} veses na frase. '.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {} '.format(frase.find('A')+1))
print('A letra A apreceu pela ultima vez na posicao {} '.format(frase.rfind('A')+1))
