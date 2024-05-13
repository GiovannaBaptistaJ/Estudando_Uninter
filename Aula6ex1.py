Linguagensprogramação = ('JavaScript', 'Rust', 'Swift', 'Python', 'Kotlin', 'Go', 'C#', 'Dart', 'Julia', 'Typescript')
print (Linguagensprogramação[3])
i = 0
while (Linguagensprogramação[i] != 'Python'):
    i += 1
print (f'Encontramos Python na posição {i}')

def func_maior(msg, *num):

    maior = 0

    for i in num:

        if i > maior:

            maior = i

    print(msg, maior)

#programa principal

func_maior('Maior: ', 8, 6, 4, 78, 56, 12, 9)



       






