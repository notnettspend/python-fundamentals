soma = 0
contador = 1

while contador <= 5:
    numero = int(input(f"Digite o {contador}º número: "))
    soma = soma + numero
    contador = contador + 1

print(f"A soma dos números é: {soma}")


soma_notas = 0
contador_notas = 1
while contador_notas <= 4:
    nota = float(input("digite a nota: "))
    soma_notas = soma_notas + nota
    contador_notas = contador_notas + 1
media = soma_notas / 4
if media >= 7.0:
    print(f"Aluno Aprovado com media {media}")
elif 5.0 <= media < 7.0:
    print(f"Aluno precisa fazer recuperação com media: {media}")
else:
    print(f"Aluno reprovado")


login = input("digite o login: ")
senha = input("digite a senha: ")

while login != "admin" or senha != "python123":
    print (f"senha ou login incorretos")
    login = input("digite o login: ")
    senha = input("digite a senha: ")
print (f"acesso permitido")


quant_funcionarios = int(input("Digite a quantidade de funcionários: "))

cont_funcionarios = 1

while cont_funcionarios <= quant_funcionarios:
    print(f"\nCadastro do funcionário {cont_funcionarios}")

    nome_funcionario = input("Digite o nome do funcionário: ")
    idade_funcionario = int(input("Digite a idade do funcionário: "))
    salario_funcionario = float(input("Digite o salário do funcionário: "))

    if salario_funcionario >= 5000 and idade_funcionario >= 25:
        print(f"{nome_funcionario} pode ocupar um cargo de liderança.")
    else:
        print(f"{nome_funcionario} ainda não pode ocupar um cargo de liderança.")

    cont_funcionarios = cont_funcionarios + 1

print("Todos os funcionários foram cadastrados.")