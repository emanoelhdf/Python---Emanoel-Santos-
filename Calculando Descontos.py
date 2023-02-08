preco = float(input('Qual é o preço do produto? R$'))
porcen = int(input('valor do desconto em porcentagem: '))
resul = preco - (preco * porcen / 100)
print('o produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(preco, porcen, resul))