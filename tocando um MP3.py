import emoji
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
res = n1 + n2
print(emoji.emojize('A soma de {} + {} é {}. :thumbs_up:'.format(n1, n2, res)))
from playsound import playsound
playsound('ex006b.mp3')