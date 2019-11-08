import random
from Agente import Agente

class Comunidad():

    #nombre

    def __init__(self, numeroAgentes, numeroAgentesEspeciales,numeroObjetos):
        #self.nombre =  nombre
        self.numeroObjetos = numeroObjetos
        self.lista_agentes = self.inicializar_agentes(numeroAgentes,numeroObjetos)
        self.lista_agentes_especiales = self.inicializar_agentes_esp(numeroAgentesEspeciales,numeroObjetos)
        self.memoria_palabras = self.list_palabras(numeroObjetos)
        self.total_palabras = self.list_palabras(numeroObjetos)
        self.total_palabras_diferentes = self.list_palabras(numeroObjetos)
        self.convergencia = self.list_conv(numeroObjetos)
        #self.list_palabras()


    def actualizar_memoria(self):
        for ys in range(0, self.numeroObjetos):
            self.memoria_palabras[ys] = []
            for xs in self.lista_agentes:
                print(xs.memoria[ys])
                self.memoria_palabras[ys] += xs.memoria[ys]
                #print(xs.memoria[ys])
            self.total_palabras[ys].append(len(self.memoria_palabras[ys]))
            diferentes = list(set(self.memoria_palabras[ys]))
            print("---------------------------")
            print(self.memoria_palabras[ys])
            print("---------------------------")
            self.total_palabras_diferentes[ys].append(len(diferentes))
            if len(diferentes) ==1 :
                total = self.memoria_palabras[ys].count(diferentes[0])
                if total == len(self.lista_agentes):
                    self.convergencia[ys]= True
                    for ts in self.lista_agentes:
                        ts.convergencia[ys] = True
        print("**************************************")



    def comunicacion_interior(self):
        for xs in range(0,self.numeroObjetos):
            for ys in self.lista_agentes:
                if self.convergencia[xs] == False:
                    agente_es = random.choice(self.lista_agentes)
                    ys.comunicacion_hablante(agente_es,xs)
                elif self.convergencia[xs] == True:
                    print("El objeto numero " + str(xs) + " se llama " + ys.memoria[xs][0] )
                    #print(agente_es.memoria[xs])
        self.actualizar_memoria()



    #def comunicacion_exterior_oyente(self, agente):

    #def comunicacion_exterior_hablante(self, agente):

    def comunicacion(self):
        while self.rev_convergencia() == False:
            self.comunicacion_interior()
        print("Convergencia")


    def rev_convergencia(self):
        for xs in self.convergencia:
            if xs == False:
                return False
        return True

    def inicializar_agentes(self,numeroAgentes,numeroObjetos):
        lista = []
        for xs in range(0,numeroAgentes):
            lista.append(Agente(0,numeroObjetos))
        return lista

    def inicializar_agentes_esp(self,numeroAgentes,numeroObjetos):
        lista = []
        for xs in range(0,numeroAgentes):
            agente_especial = Agente(1, numeroObjetos)
            self.lista_agentes.append(agente_especial)
            lista.append(agente_especial)
        return list

    def list_palabras(self,numObjetos):
        lista = []
        for xs in range(0,numObjetos):
            lista.append(list())
        return lista

    def list_conv(self,numObjetos):
        lista = []
        for xs in range(0,numObjetos):
            lista.append(False)
        return lista


#comunidad1 = Comunidad(5,1,5)
#comunidad1.comunicacion()
