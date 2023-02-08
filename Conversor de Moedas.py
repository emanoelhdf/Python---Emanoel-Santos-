real = float(input('Quanto reias eu tenho na carteira: R$'))
dolar = float(input('cotação atual do dolar: US$'))
r = real / dolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, r))