salario = float(input('Qual é o salário do Funcionário? R$'))
porcen = float(input('Quantos porcento de aumento? %'))
aumen = salario + (salario * porcen / 100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, porcen, aumen))
