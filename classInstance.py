class Person:
    def __init__(self,initialAge):

        if initialAge < 0:
            self.age = 0
            print ('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge

    def amIOld(self):

        if self.age < 13:
            print ('You are young.')
        elif  13 <= self.age < 18:
            print ('You are a teenager.')
        else:
            print ('You are old.')

    def yearPasses(self):
        self.age = self.age + 1


if __name__ == '__main__':

    age = int(input('Introduce tu edad: '))
    p = Person(age) #instanciamos la clase Person
    #Ya podemos ejecutar sus metodos
    p.amIOld()

    for j in range(0, 3):
        p.yearPasses()

    p.amIOld()

