class Darbuotojai:

    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atllyginimas = '| ' + 'Atlyginimas - ' + atlyginimas + ' Eurų\n'
        self.email = 'El paštas : ' + vardas + '.' + pavarde + '@_______.lt'

    def pilnasvardas(self):
        print('{} {}'.format(self.vardas,self.pavarde))

    def duomenys(self):
        print('{} {} {} {}'.format(self.vardas, self.pavarde, self.atllyginimas, self.email))
        # atllyginimas ne atlyginimas

user_1 = Darbuotojai('Vardenis', 'Pavardenis', '4854')
user_2 = Darbuotojai('Vardenė', 'Pavardenė', '7910')


# Darbuotojai.pilnasvardas(user_1)
Darbuotojai.duomenys(user_2)
