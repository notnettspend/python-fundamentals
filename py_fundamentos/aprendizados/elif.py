nota1 = float(input("digite a primeira nota do aluno: "))
nota2 = float(input("digite a segunda nota do aluno: "))
nota3 = float(input("digite a terceira nota do aluno: "))
nota4 = float(input("digite a quarta nota do aluno: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6.0:
    print("Aluno aprovado com média:", media)
elif 6.0 > media >= 4.0:
    print("Aluno em recuperação com média:", media)
else:
    print("Aluno reprovado com média:", media)