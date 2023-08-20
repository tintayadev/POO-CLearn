class Pelicula:

    def __init__(self, nombre, ano):
            self.nombre = nombre
            self.ano = ano

    def posterior(self, gestion):
        if self.ano >= gestion:
            return True
        else:
            return False


class Usuario:

    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    def pass_fragil(self):

        nums = "0123456789"
        # buscar si es que hay al menos un numero en self.contrasena
        encontrado = False
        for c in self.contrasena:
            if c in nums:
                encontrado = True
        if len(self.contrasena) < 8 or not encontrado:
            return True
        else:
            return False


class Nerdflix:

    def __init__(self):
        self.peliculas = []
        self.usuarios = []
        self.visualizaciones = []

    def agregar_usuario(self, u):
        self.usuarios.append(u)

    def agregar_pelicula(self, p):
        self.peliculas.append(p)

    def peli_disponible(self, n):
        for elem in self.peliculas:
            if n == elem.nombre:
                return True
        return False

    def users_fragiles(self):
        lista_fragil = []
        for usuario in self.usuarios:
            if usuario.pass_fragil():
                lista_fragil.append(usuario.nombre)
        return lista_fragil

    def nuevo_visionado(self, u, p):
        nuevo = [u, p]
        self.visualizaciones.append(nuevo)


    def max_visionador(self, n):
        def comparar_visualizaciones(registro):
            return registro[1]
        registros = []
        for usuario, pelicula in self.visualizaciones:
            if pelicula.nombre == n:
                encontrado = False
                for registro in registros:
                    if registro[0] == usuario.nombre:
                        registro[1] += 1
                        encontrado = True
                        break
                if not encontrado:
                    registros.append([usuario.nombre, 1])
        
        if not registros:
            return ""
        
        max_visualizaciones = max(registros, key=comparar_visualizaciones)[1]
        usuario_max_visionador = ""
        
        for usuario, visualizaciones in registros:
            if visualizaciones == max_visualizaciones:
                if not usuario_max_visionador or len(usuario) < len(usuario_max_visionador):
                    usuario_max_visionador = usuario

        return usuario_max_visionador


        # def por_numero(lista):
        #     return lista[1]
        # # def porLen(nombre):
        # #     return len(nombre) 
        # sw = True
        # registros = []#[["ejemplo", 0]]
        # for visualizacion in self.visualizaciones:
        #     u = visualizacion[0]    # Usuario
        #     p = visualizacion[1]    # Pelicula
        #     if n == p.nombre:    # B
        #         # busqueda de nombre en la lista registro
        #         if sw:
        #             registros.append([u.nombre,1])
        #             sw = False
        #         else:
        #             for registro in registros:
        #                 if u.nombre == registro[0]:    # revisar si es que u.nombre esta ya registrado
        #                     registro[1] += 1
        #                 else:    # en caso de que no este registrado
        #                     subregistro = [u.nombre, 1]
        #                     registros.append(subregistro)
        
        # if registros == []:
        #     return ""
        # if len(registros) == 1:
        #     return registros[0][0]
        # #aqui
        # registros.sort(key=por_numero)
        # print(registros, "========================")
        # may = registros[len(registros)-1][1]
        # cnt = 0
        # nombres_max = []
        # for r in registros:
        #     if r[1] == may:
        #         cnt += 1
        #         nombres_max.append(r[0])
        

        # if cnt == 1:
        #     return registros[-1][0]
        # else:
        #     nombres_max.sort(key=len)
        #     return nombres_max[0]
        
n = Nerdflix()

u1 = Usuario('Christopher Williams', 'mfSVXo78')
u2 = Usuario('Rachael Ruiz', 'jFKNdqOE')
u3 = Usuario('Alexis Khan', 'JTNkCez10')
u4 = Usuario('Curtis Jackson', 'dLRUu5')
u5 = Usuario('Jesus Rogers', 'zVemKgBPn62')
u6 = Usuario('Jennifer Vasquez', 'gRdIKQvp0')

p1 = Pelicula('Silver Linings Playbook', 2012)
p2 = Pelicula('Searching for Sugar Man', 2012)
p3 = Pelicula('Scott Pilgrim vs. the World', 2010)
p4 = Pelicula('Atlantics', 2019)

n.agregar_usuario(u1)
n.agregar_usuario(u2)
n.agregar_usuario(u3)
n.agregar_usuario(u4)
n.agregar_usuario(u5)
n.agregar_usuario(u6)
n.agregar_pelicula(p1)
n.agregar_pelicula(p2)
n.agregar_pelicula(p3)
n.agregar_pelicula(p4)

n.nuevo_visionado(u1,p4)
n.nuevo_visionado(u3,p2)
n.nuevo_visionado(u5,p2)
n.nuevo_visionado(u4,p1)
n.nuevo_visionado(u2,p3)
n.nuevo_visionado(u2,p1)
n.nuevo_visionado(u3,p4)
n.nuevo_visionado(u5,p4)
n.nuevo_visionado(u2,p1)
n.nuevo_visionado(u3,p2)
n.nuevo_visionado(u2,p3)
n.nuevo_visionado(u1,p4)

print(n.max_visionador('Silver Linings Playbook'))
print(n.max_visionador('Searching for Sugar Man'))
print(n.max_visionador('Scott Pilgrim vs. the World'))
print(n.max_visionador('Atlantics'))  


for x in n.peliculas:
    print(x.nombre, x.ano, " - ", end="")
print()
for x in n.usuarios:
    print(x.nombre, x.contrasena, " - ", end="")
print()
for x in n.visualizaciones:
    print(x[0].nombre, x[1].nombre)
