from Sociedad import Sociedad
import os

numComunidades = 2
numeroAgentes = 19
numeroAgentesEspeciales = 1
numeroObjetos = 2
direccion = "experimento"

for xs in range (2, 10):
    direccion = "experimento"
    direccion = direccion + "_" + str(xs) + "_" + str(numeroAgentes) + "_" + str(numeroAgentesEspeciales) + "_" + str(numeroObjetos)
    if not os.path.exists(direccion):
        os.makedirs(direccion+'/')
    sociedad = Sociedad(xs, numeroAgentes, numeroAgentesEspeciales,numeroObjetos,direccion)
    sociedad.experimento()


for xs in range (19, 29):
    direccion = "experimento"
    direccion = direccion + "_" + str(numComunidades) + "_" + str(xs) + "_" + str(numeroAgentesEspeciales) + "_" + str(numeroObjetos)
    if not os.path.exists(direccion):
        os.makedirs(direccion+'/')
    sociedad = Sociedad(numComunidades, xs, numeroAgentesEspeciales,numeroObjetos,direccion)
    sociedad.experimento()


for xs in range (1, 10):
    direccion = "experimento"
    direccion = direccion + "_" + str(numComunidades) + "_" + str(numeroAgentes) + "_" + str(xs) + "_" + str(numeroObjetos)
    if not os.path.exists(direccion):
        os.makedirs(direccion+'/')
    sociedad = Sociedad(numComunidades, numeroAgentes, numeroAgentesEspeciales,xs,direccion)
    sociedad.experimento()

for xs in range (2, 12):
    direccion = "experimento"
    direccion = direccion + "_" + str(xs) + "_" + str(numeroAgentes) + "_" + str(numeroAgentesEspeciales) + "_" + str(xs)
    if not os.path.exists(direccion):
        os.makedirs(direccion+'/')
    sociedad = Sociedad(numComunidades, numeroAgentes, numeroAgentesEspeciales,numeroObjetos,xs)
    sociedad.experimento()
