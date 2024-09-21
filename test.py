loteria = [3, 42, 12, 19, 30, 59]
print(loteria)
loteria.reverse()
print(loteria)
print(loteria[0])
loteria.append(199)
print(loteria)
loteria = [6, 7, 1000, -1, -6, -1000]
print(loteria[0])
loteria.pop(0)
print(loteria)
ucastnicka = {'meno': 'Andrea', 'krajina': 'Slovensko', 'oblubene_cisla':[1, 11, 4, 8]}
print(ucastnicka['meno'])
print(ucastnicka['krajina'])
print(ucastnicka['oblubene_cisla'])
print(ucastnicka['oblubene_cisla'][0])
len(ucastnicka)
ucastnicka['oblubeny_jazyk'] = 'Python'
print(ucastnicka)
ucastnicka['krajina'] = 'Nemecko'
print(ucastnicka)
def andrea():
    print('Cau!')
    print('Ako sa máš?')
andrea()
def anna(cislo):
    if cislo == '1':
        print ('cislo 1')
    elif cislo=='2':
        print('cislo == 2')
    else:
        print('nezname cislo')
anna('3')


def ahoj(meno):
    print('Ahoj ' + meno + '!')
dievcata = ['Katka', 'Kika', 'Zuza', 'Ola', 'Ty']
for meno in dievcata:
    ahoj(meno)
    print('Dalsie dievca')