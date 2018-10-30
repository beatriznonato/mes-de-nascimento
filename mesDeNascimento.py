mesesDoAno = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
dataNascimento = input('Informe sua data de nascimento no formato DD-MM-AAAA: ')

indice = int(dataNascimento[3:5])-1
mes = mesesDoAno[indice]

print('Você nasceu no mês de',mes)
