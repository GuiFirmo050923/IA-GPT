# Média do aluno
nome = input("Digite o nome do aluno: ")
print(f"Nome do aluno {nome}")

nota_01 = float(input("Nota 01 do aluno: "))
nota_02 = float(input("Nota 02 do aluno: "))
nota_03 = float(input("Nota 03 do aluno: "))
nota_04 = float(input("Nota 04 do aluno: "))

media_aluno = (nota_01 + nota_02 + nota_03 + nota_04)/4
print(f"A média do aluno é: {media_aluno}")

if media_aluno >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
