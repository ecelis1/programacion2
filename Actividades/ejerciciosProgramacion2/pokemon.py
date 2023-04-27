class Pokemon:
    def __init__(self, nombre,color,potenciaAtaque,nivelVida):
        self.nombre = nombre
        self.color = color
        self.potenciaAtaque = potenciaAtaque
        self.nivelVida = nivelVida
    
    def saludar(self):
        print(f'SOY {self.nombre} Y QUIERO QUE ME USES PARA PELEAR')

    def sanar(self):
        nivelVida = int(self.nivelVida)+20
        
        self.nivelVida = str(nivelVida)

    def aumentarAtaque(self):
        
        niveldeAtaque = int(self.potenciaAtaque)
        self.potenciaAtaque = str(int(self.potenciaAtaque)+(niveldeAtaque*0.20))


class porDefault(Pokemon):
    def __init__(self, nombre, color, potenciaAtaque, nivelVida):
        super().__init__(nombre, color, potenciaAtaque, nivelVida)

        self.nombre = nombre
        self.color = color
        self.potenciaAtaque = potenciaAtaque
        self.nivelVida = nivelVida

class parametrosEspeficicos(Pokemon):
    def __init__(self, nombre, color, potenciaAtaque, nivelVida):
        super().__init__(nombre, color, potenciaAtaque, nivelVida)
        
        self.nombre = nombre
        self.color = color
        self.potenciaAtaque = potenciaAtaque       
        self.nivelVida = nivelVida

def menu():
    print('POKEMON\n1-Agregar pokemon con atributos por Default\n2-Agregar Pokemon con atributos especificos\n3- SALIR\nIngrese su seleccion: ')


def main():
    while True:
        seleccion=int(input(menu()))
        

        match seleccion:
            case 1:
                print('CREANDO POKEMON CON ATRIBUTOS POR DEFAULT')
                nombre = input('Ingrese el nombre del Pokemon: ')
                color = 'Azul'
                potenciaAtaque = '100'
                nivelVida = '100'
                pokemon1 = porDefault(nombre,color,potenciaAtaque,nivelVida)

                print(f'Se ha creado el pokemon con atributos por default con exito\nNombre:{pokemon1.nombre}\nColor: {pokemon1.color}\nPotencia de Ataque: {pokemon1.potenciaAtaque}\nNivel de Vida: {pokemon1.nivelVida}')

                pokemon1.saludar()
            
            case 2:
                print('CREANDO POKEMON CON ATRIBUTOS ESPEFICICOS')
                nombre = input('Ingrese el nombre del Pokemon: ')
                color = input('Ingrese el color: ')
                potenciaAtaque = input('Ingrese Potencia de Ataque: ')
                nivelVida = input('Ingrese el nivel de Vida: ')

                pokemon1 = parametrosEspeficicos(nombre,color,potenciaAtaque,nivelVida)

                print(f'Se ha creado el pokemon con atributos por default con exito\nNombre:{pokemon1.nombre}\nColor: {pokemon1.color}\nPotencia de Ataque: {pokemon1.potenciaAtaque}\nNivel de Vida: {pokemon1.nivelVida}')

                pokemon1.saludar()

                acciones = int(input('Que quieres hacer conmigo?\n1- CURARME\n2-AUMENTAR MI ATAQUE\nIngrese una opcion: '))
                match acciones:
                    case 1:
                        pokemon1.sanar()
                        print(f'El pokemon se ha curado con exito\nNombre:{pokemon1.nombre}\nNivel de Vida: {pokemon1.nivelVida}')
                    case 2:
                        pokemon1.aumentarAtaque()
                        print(f'Se ha aumentado el poder de ataque del pokemon\nNombre:{pokemon1.nombre}\nPotencia de Ataque: {pokemon1.potenciaAtaque}')
                    case default:
                        print('Ingrese una opcion correcta')
            case 3:
                print('Usted ha salido')
                break

            case default:
                print('Ingrese una seleccion correcta (1,2,3)')

if __name__ == '__main__':
    main()