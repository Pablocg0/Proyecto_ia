import pandas as df


class Agente():

    maxPalabras = 10


    def __init__(self,especial,numObjetos):
        self.especial = especial
        self.memoria= self.list_palabras(10)
        self.convergencia = self.list_convergencia(numObjetos)


    def comunicacion_hablante_especial(self, agente, numObjeto):
        if self.convergencia[numObjeto] :
            palabra_enviada = self.memoria[numObjeto][0]
            respuesta = agente.comunicacion_oyente_especial(palabra_enviada, numObjeto, self.convergencia[numObjeto])
            if respuesta == True:
                print("Ambas comunidades encontraron el nombre para el objeto " + str(numObjeto) + " con el nombre de "+ palabra_enviada)
            else:
                print("La comunidad oyente no ha convergido para la palabra "+ palabra_enviada)
        else:
            palabra_enviada = self.memoria[numObjeto][0]
            respuesta = agente.comunicacion_oyente_especial(self.memoria[numObjeto][0], numObjeto,self.convergencia[numObjeto])
            if respuesta == True:
                self.memoria[numObjeto] = []
                self.memoria[numObjeto].append(palabra_enviada)
            elif respuesta == False:
                self.memoria[numObjeto].pop(len(self.memoria[numObjeto])-1)
                self.memoria[numObjeto].append(self.obtener_palabra())
            elif type(respuesta) == str:
                print("str")
                self.memoria[numObjeto] = []
                self.memoria[numObjeto].append(respuesta)
                self.convergencia[numObjeto] = False



    def comunicacion_hablante(self, agente, numObjeto):
        print(self.memoria[numObjeto])
        if len(self.memoria[numObjeto])==0 :
            nueva_palabra = self.obtener_palabra()
            #print(nueva_palabra)
            self.memoria[numObjeto].append(nueva_palabra)
        else:
            palabra_enviada = self.memoria[numObjeto][0]
            respuesta = agente.comunicacion_oyente(self.memoria[numObjeto][0], numObjeto)
            if respuesta == True:
                self.memoria[numObjeto] = []
                self.memoria[numObjeto].append(palabra_enviada)
            elif respuesta == False:
                self.memoria[numObjeto].pop(0)
                nueva_palabra = self.obtener_palabra()
                #print(nueva_palabra)
                self.memoria[numObjeto].append(nueva_palabra)

    def comunicacion_oyente_especial(self, palabra, numObjeto, convergencia):
        if self.convergencia[numObjeto] == True and convergencia == False:
            return self.memoria[numObjeto][0]
        elif self.convergencia[numObjeto] == False and convergencia == False or convergencia == True:
            if palabra in self.memoria[numObjeto]:
                self.memoria[numObjeto] = []
                self.memoria[numObjeto].append(palabra)
                return True
            else:
                if len(self.memoria[numObjeto]) == 2*self.maxPalabras:
                    self.memoria[numObjeto] = []
                    self.memoria[numObjeto].append(palabra)
                    return False
                else:
                    self.memoria[numObjeto].insert(0,palabra)
                    return False
        elif self.convergencia[numObjeto] == True and convergencia == True:
            self.memoria[numObjeto]=[]
            self.memoria[numObjeto].append(palabra)
            self.convergencia[numObjeto] = False
            return True

    def comunicacion_oyente(self, palabra, numObjeto):
        if self.especial == 1:
            if palabra in self.memoria[numObjeto]:
                self.memoria[numObjeto] = []
                self.memoria[numObjeto].append(palabra)
                return True
            else:
                if len(self.memoria[numObjeto]) == 2*self.maxPalabras:
                    self.memoria[numObjeto] = []
                    self.memoria[numObjeto].append(palabra)
                    return False
                else:
                    self.memoria[numObjeto].append(palabra)
                    self.convergencia[numObjeto] =False
                    return False
        elif self.especial == 0:
            if palabra in self.memoria[numObjeto]:
                self.memoria[numObjeto] = []
                self.memoria[numObjeto].append(palabra)
                return True
            else:
                if len(self.memoria[numObjeto]) == self.maxPalabras:
                    self.memoria[numObjeto] = []
                    self.memoria[numObjeto].append(palabra)
                    return False
                else:
                    self.memoria[numObjeto].append(palabra)
                    self.convergencia[numObjeto] =False
                    return False


    def comunicacion_oyente_2(self, palabra, numObjeto):
        if len(self.memoria[numObjeto]) == self.maxPalabras:
            self.memoria[numObjeto].pop(0)
            self.memoria[numObjeto].append(palabra)
            return True
        else:
            if palabra in self.memoria[numObjeto]:
                self.memoria[numObjeto] = []
                self.memoria[numObjeto].append(palabra)
                return True
            else:
                self.memoria[numObjeto].append(palabra)
                return False


    def list_convergencia(self,numObjetos):
        conv = []
        for xs in range(0,numObjetos):
            conv.append(False)
        return conv

    def obtener_palabra(self):
        diccionario = df.read_csv("dick.csv")
        palabra = diccionario["a"].sample(n=1)
        return palabra.iloc[0]


    def list_palabras(self,numObjetos):
        mem = []
        for xs in range(0,numObjetos):
            mem.append(list())
        return mem
