from Comunidad import Comunidad
import random
import pandas as df

class Sociedad():




    def __init__(self, numComunidades, numeroAgentes, numeroAgentesEspeciales, numObjetos, direccion):
        self.direccion
        self.numeroAgentes = numeroAgentes
        self.numeroAgentesEspeciales = numeroAgentesEspeciales
        self.numeroObjetos = numObjetos
        self.numComunidades = numComunidades
        self.lista_comunidades = self.inicializar_comunidades(numComunidades, numeroAgentes, numeroAgentesEspeciales, numObjetos)
        self.memoria_palabras = self.inicializar_listas(numObjetos)
        self.total_palabras = self.inicializar_listas(numObjetos)
        self.total_palabras_diferentes = self.inicializar_listas(numObjetos)
        self.convergencia = self.inicializar_conv(numObjetos)


    def actualizar_memoria(self):
        for xs in range(0,self.numeroObjetos):
            self.memoria_palabras[xs] = []
            for ys in self.lista_comunidades:
                #print(ys.memoria_palabras[xs])
                self.memoria_palabras[xs] += ys.memoria_palabras[xs]
            self.total_palabras[xs].append(len(self.memoria_palabras))
            diferentes = list(set(self.memoria_palabras[xs]))
            self.total_palabras_diferentes[xs].append(len(diferentes))
            print("///////////////////////////////")
            print(self.memoria_palabras[xs])
            print(diferentes)
            print("///////////////////////////////")

            print()
            if len(diferentes) ==1 :
                total = self.memoria_palabras[xs].count(diferentes[0])
                print("-----------------------------------------")
                print(str(total))
                print("-----------------------------------------")
                if total == len(self.lista_comunidades*(self.numeroAgentes+self.numeroAgentesEspeciales)):
                    self.convergencia[xs]= True

    def guardar_datos(self):
        lista_palabras = self.total_palabras
        lista_palabras_totales = self.total_palabras_diferentes
        print(lista_palabras)
        for xs in range(0,sociedad.numeroObjetos):
            lis  = df.DataFrame(lista_palabras[xs], columns=["totalPalabras"])
            lis2  = df.DataFrame(lista_palabras_totales[xs], columns=["totalPalabrasDiferentes"])
            total = df.concat([lis,lis2], axis=1)
            total.to_csv(self.direccion+ "/data_sociedad_objeto_"+str(xs)+"_X.csv",encoding='utf-8',index=False)
        comunidad = 0
        for xs in sociedad.lista_comunidades:
            lista_palabras = xs.total_palabras
            lista_palabras_totales = xs.total_palabras_diferentes
            for ys in range(0,sociedad.numeroObjetos):
                lis  = df.DataFrame(lista_palabras[ys], columns=["totalPalabras"])
                lis2  = df.DataFrame(lista_palabras_totales[ys], columns=["totalPalabrasDiferentes"])
                total = df.concat([lis,lis2], axis=1)
                total.to_csv(self.direccion +"/data_comunidad_objeto_"+str(ys)+"_"+str(comunidad)+"_.csv",encoding='utf-8',index=False)
                comunidad +=1



    def comunicacion(self):
        for xs in self.lista_comunidades:
            xs.comunicacion_interior()
        for ys in range(0, self.numeroObjetos):
            num_ale = random.randint(self.numeroAgentes, (self.numeroAgentes+self.numeroAgentesEspeciales)-1)
            num_ale_1 = random.randint(self.numeroAgentes, (self.numeroAgentes+self.numeroAgentesEspeciales)-1)
            num_ale_2 = random.randint(0,self.numComunidades-1)
            xs.lista_agentes[num_ale].comunicacion_hablante_especial(self.lista_comunidades[num_ale_2].lista_agentes[num_ale_1],ys)
        self.actualizar_memoria()
        print("###################################################################")

    def experimento(self):
        while self.rev_convergencia() == False:
            self.comunicacion()
        print("Convergencia")

    def rev_convergencia(self):
        for xs in self.convergencia:
            if xs == False:
                return False
        return True


    def inicializar_comunidades(self,numComunidades,numeroAgentes, numeroAgentesEspeciales, numObjeto):
        lista = []
        for xs in range(0,numComunidades):
            lista.append(Comunidad(numeroAgentes, numeroAgentesEspeciales, numObjeto))
        return lista

    def inicializar_listas(self,numObjetos):
        listas = []
        for xs in range(0,numObjetos):
            listas.append(list())
        return listas

    def inicializar_conv(self,numObjetos):
        lista = []
        for xs in range(0,numObjetos):
            lista.append(False)
        return lista


direccion =

def save_data(sociedad, indice):
    lista_palabras = sociedad.total_palabras
    lista_palabras_totales = sociedad.total_palabras_diferentes
    print(lista_palabras)
    for xs in range(0,sociedad.numeroObjetos):
        lis  = df.DataFrame(lista_palabras[xs], columns=["totalPalabras"])
        lis2  = df.DataFrame(lista_palabras_totales[xs], columns=["totalPalabrasDiferentes"])
        total = df.concat([lis,lis2], axis=1)
        total.to_csv(direccion+"/data_sociedad_objeto_"+str(xs)+"_"+ str(indice)+".csv",encoding='utf-8',index=False)
    comunidad = 0
    for xs in sociedad.lista_comunidades:
        lista_palabras = xs.total_palabras
        lista_palabras_totales = xs.total_palabras_diferentes
        for ys in range(0,sociedad.numeroObjetos):
            lis  = df.DataFrame(lista_palabras[ys], columns=["totalPalabras"])
            lis2  = df.DataFrame(lista_palabras_totales[ys], columns=["totalPalabrasDiferentes"])
            total = df.concat([lis,lis2], axis=1)
            total.to_csv(direccion+"/data_comunidad_objeto_"+str(ys)+"_"+ str(indice)+"_"+str(comunidad)+".csv",encoding='utf-8',index=False)
            comunidad +=1


 if not os.path.exists(direccion):
        os.makedirs(direccion'/')
        
sociedad =  Sociedad(3,5,1,2, direccion)
sociedad.experimento()
save_data(sociedad,0)
