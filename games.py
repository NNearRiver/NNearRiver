class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"{self.nombre} dice: ¡Hola! ¿Cómo estás?")

    def caminar_adelante(self):
        print(f"{self.nombre} camina hacia adelante.")
     
    def interactuar(self):
        print(f"{self.nombre} dice: Lo siento")
     
    def hablar(self):
        print(f"{self.nombre} dice: Vamos a la laguna")
        
    def comer_alimento(self):
        print(f"{self.nombre} come un alimento")
           
class Enemigo(Personaje):
    def __init__(self, nombre_enemigo):
        super().__init__(nombre_enemigo)

    def atacar(self):
        print(f"{self.nombre} ataca con furia.")
        
    def interactuar(self):
        print(f"{self.nombre} dice: Enserio, discúlpame")
        
    def hablar(self):
        print(f"{self.nombre} dice: Te sigo")
        
    def comer_alimento(self):
        print(f"{self.nombre} come un alimento") 

# Crear instancias de las clases
jugador = Personaje("Ford")
enemigo = Enemigo("George")

# Interactuar con los personajes
jugador.saludar()
enemigo.saludar()

jugador.caminar_adelante()
enemigo.caminar_adelante()

enemigo.atacar()

jugador.interactuar()
enemigo.interactuar()

jugador.hablar()
enemigo.hablar()

jugador.comer_alimento()
enemigo.comer_alimento()

