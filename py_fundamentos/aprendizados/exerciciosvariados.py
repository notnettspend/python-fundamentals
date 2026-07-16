alunos = 420
professores = 28
funcionarios_administrativos = 15

total_pessoas_escola = alunos + professores + funcionarios_administrativos
print ("total de pessoas na escola:", total_pessoas_escola)

aluno_por_professor = alunos / professores 
print ("quantidade de aluno por professor:", aluno_por_professor)


notebook = 4200
mouse = 150
teclado = 320

faturamento_notebook = notebook * 12
print ("faturamento dos notebooks:", faturamento_notebook)

faturamento_mouse = mouse * 45
print ("faturamento dos mouses:", faturamento_mouse)

faturamento_teclado = teclado * 30
print ("faturamento dos teclados:", faturamento_teclado)

faturamento_total = faturamento_notebook + faturamento_mouse + faturamento_teclado
print ("faturamento total:", faturamento_total)

rh_funcionarios = 8
ti_funcionarios = 15
financeiro_funcionarios = 10
marketing_funcionarios = 12
rh_salario = 4200
ti_salario = 7800
financeiro_salario = 5600
marketing_salario = 4800

total_funcionarios = rh_funcionarios + ti_funcionarios + financeiro_funcionarios + marketing_funcionarios
print ("total de funcionarios:", total_funcionarios)

fs_ti = ti_funcionarios * ti_salario
print ("folha salarial de ti:", fs_ti)

fs_financeiro = financeiro_funcionarios * financeiro_salario
print ("folha salarial do financeiro:", fs_financeiro)

fs_rh = rh_funcionarios * rh_salario
print ("folha salarial do rh:", fs_rh)

fs_marketing = marketing_funcionarios * marketing_salario
print ("folha salarial do marketing:", fs_marketing)

fs_empresa = fs_ti + fs_financeiro + fs_rh + fs_marketing
print ("folha salarial total da empresa:", fs_empresa)

