nome = input("escreva seu nome:")
idade = int(input("escreva a sua idade:"))
cidade = input("escreva a sua cidade:")

print("seu nome é:", nome, "voce tem:", idade, "e sua cidade é:", cidade)


quantidade_rh = int(input("escreva a quantidade de pessoas do RH:"))
quantidade_ti = int(input("escreva a quantidade de pessoas do TI:"))
quantidade_fin = int(input("escreva a quantidade de pessoas do financeiro:"))

total_funcionarios = quantidade_rh + quantidade_ti + quantidade_fin
print("o total de funcionarios é:", total_funcionarios)

porcentagem_rh = quantidade_rh / total_funcionarios * 100
print("a porcentagem de pessoas do RH é:", porcentagem_rh)

porcentagem_ti = quantidade_ti / total_funcionarios * 100
print("a porcentagem de pessoas do TI é:", porcentagem_ti)

porcentagem_fin = quantidade_fin / total_funcionarios * 100
print("a porcentagem de pessoas do financeiro é:", porcentagem_fin)


prdigitarnumero = int(input("digite um numero:"))
sgdigitarnumero = int(input("digite outro numero:"))
somadosnumeros = prdigitarnumero + sgdigitarnumero
print("a soma dos numeros é:", somadosnumeros)


nota1 = float(input("digite a primera nota:"))
nota2 = float(input("digite a segunta nota:"))
nota3 = float(input("digite a segunda nota:"))
nota4 = float(input("digite a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4) / 4
print ("a media das notas é:", media)


quantidadecvs = int(input("digite a quantiadade de cvs:"))
quantidadelinhas = int(input("digite a quantindade de linhas:"))
totalinhas = quantidadecvs * quantidadelinhas
print("o total de linhas é:", totalinhas)

quantidadecolunas = int(input("digite a quantidade de colunas:"))
totalcelulas = totalinhas * quantidadecolunas
print("o total de celulas é:", totalcelulas)


preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))
faturamento = preco_produto * quantidade_produto
print("O faturamento é:", faturamento)
desconto = int(input("Digite o percentual de desconto: "))
valor_do_desconto = (desconto * faturamento) / 100
print("O valor do desconto é:", valor_do_desconto)
faturamento_com_desconto = faturamento - valor_do_desconto
print("O faturamento com desconto é:", faturamento_com_desconto)