nome = input("digite o nome do aluno: ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))
mediadenota = (nota1 + nota2 + nota3 + nota4) / 4
if mediadenota >= 6:
    print(f"aluno {nome} aprovado!")
else:
    print(f"aluno {nome} reprovado!")


nome2 = input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))
if idade >= 18:
    print(f"{nome2} você é maior de idade!")
else:
    print(f"{nome2} você é menor de idade!")


temperatura = int(input("digite a temperatura atual: "))
if temperatura >= 30:
    print("está muito quente!")
else:
    print("está frio!")


nome3 = input("digite o nome do funcionario: ")
salario = float(input("digite o salario do funcionario: "))
if salario >= 5000:
    print(f"O funcionario {nome3} esta elegivel para bonus")
else:
    print(f"O funcionario {nome3} nao esta elegivel para bonus")


produto = input("digite o nome do produto: ")
qtproduto = int(input(" digite a quantidade do produto no estoque: "))
if qtproduto <= 10:
    print(f"O produto {produto} esta em falta no estoque")
else:
    print(f"O produto {produto} esta disponivel no estoque")


nome4 = input("digite o nome do funcionario: ")
idade2 = int(input("digite a idade do funcionario: "))
salario2 = int(input("digite o salario do funcionario: "))
if salario2 >= 7000:
    print(f"O funcionario {nome4} de idade {idade2} possui um salario alto")
else:
    print(f"O funcionario {nome4} de idade {idade2} possui um salario baixo")


temperaturasp = int(input("digite a temperatura atual do estado de sao paulo: "))
if temperaturasp >= 30:
    print(f"Sao Paulo esta em alerta de calor")
else:
    print(f"Sao Paulo esta em alerta de frio")


nota5 = float(input("digite a primeira nota do aluno: "))
nota6 = float(input("digite a segunda nota do aluno: "))
nota7 = float(input("digite a terceira nota do aluno: "))
nota8 = float(input("digite a quarta nota do aluno: "))
nota9 = float(input("digite a quinta nota do aluno: "))
mediadoaluno = (nota5 + nota6 + nota7 + nota8 + nota9) / 5
if mediadoaluno >= 6:
    print(f"O aluno esta aprovado com media {mediadoaluno}")
else:
    print(f"O aluno esta reprovado com media {mediadoaluno}")


produto2 = input("digite o nome do produto: ")
valor_venda = float(input("digite o valor de venda do produto: "))
if valor_venda >= 1000:
    print(f"Venda de alto valor")
else:
    print(f"Venda de baixo valor")


nome5= input("digite o nome do funcionario: ")
idade3 = int(input("digite a idade do funcionario: "))
salario3 = float(input("digite o salario do funcionario: "))
desempenho = int(input("digite o desempenho do funcionario (1 a 5): "))
if desempenho >= 6:
    print(f"O funcionario {nome5} esta elegivel para promoção")
else:
    print(f"O funcionario {nome5} nao esta elegivel para promoção")