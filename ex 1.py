Alunos = []
Notas = []
for Alunos in range (5):
    for Notas in range (5):
        Alunos.append(str(input(" Quais são os alunos?")))
        Notas.append(float(input( "Qual é a nota de ambos?")))

if Notas >= 7:
    print (f"{Alunos} foi aprovado")
elif Notas < 6.9:
    print (f"{Alunos} está de recuperação")
elif Notas < 4:
    print (f"{Alunos} está reprovado")
