medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print('A medida de {}m corresponde a \n{:.3f}Km\n{:.0f}cm \n{:.0f}mm'.format(medida, km, cm, mm))