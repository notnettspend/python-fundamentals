idade= int(input("Digite sua idade: "))
if idade < 13:
    print ("Voce é criança")
elif 13 <= idade <= 17:
    print ("Voce é adolescente")
elif 18 <= idade <= 59:
    print ("Voce é adulto")
else:
    print ("voce é idoso")


nomealuno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >=  7.0:
    print (f"O aluno {nomealuno} foi aprovado com média {media}")
elif 5.0 > media >= 7.0:
    print (f"O aluno {nomealuno} esta de recuperação com média {media}")
else:
    print (f"O aluno {nomealuno} esta reprovado")


nomefuncionario = input("digite o nome do funcionario: ")
idadefuncionario = int(input("digite a idade do funcionario"))
salariofuncionario = int(input("digite o salario do funcionario: "))
if salariofuncionario >= 5000 and idadefuncionario >= 25:
    print (f"O funcionario {nomefuncionario} pode ocupar o cargo de liderança")
else:
    print(f"O funcionario {nomefuncionario} ainda nao poode ocupar o cargo de liderança")


login = input("Usuario: ")
senha = input("Senha: ")
if login == "admin" and senha == "python123":
    print(f"login realizado com sucesso")
else:
    print(f"usuario ou senha invalidos")


idade_emprestimo = int(input("digite sua idade: "))
salario_emprestimo = float(input("digite seu salario: "))
if idade_emprestimo >= 18 and salario_emprestimo >= 2500:
    print(f"voce pode solicitar um emprestimo")
else:
    print(f"voce nao pode solicitar um emprestimo")


idade_festa = int(input("digite a sua idade: "))
permissao_pais = input("voce tem a permissao dos seus pais: ")
if idade_festa >=18 or permissao_pais == "sim":
    print(f"voce pode ir a festa!")
else:
    print(f"voce nao pode ir a festa!")


pedirsalario = float(input("digite o salario: "))
if pedirsalario < 2000:
    print (f"baixa renda")
elif 2000 <= pedirsalario <= 5000:
    print(f"renda media")
else:
    print(f"alta renda")


idadesolicitacao = int(input("digite a sua idade: "))
if not idadesolicitacao <0:
    print (f"idade invalida")
else:
    print (f"idade valida")