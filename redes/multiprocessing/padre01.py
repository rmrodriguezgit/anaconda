import time
import random
import multiprocessing

class tarea:

    def __init__(self, cid):
        self.__cid=cid
        print("HIJO {0} - Nace".format(self.__cid))

    def __del__(self):
        print("HIJO {0} - Muere".format(self.__cid))

    def run(self):

        # Generamos un tiempo de espera aleatorio
        s=1+int(10*random.random())

        print("HIJO {0} - Inicio (Durmiendo {1} segundos)".format(self.__cid,s))
        time.sleep(s)
        print("HIJO {0} - Fin".format(self.__cid))

# Creamos la piscina (Pool)
piscina = []
for i in range(1,5):
    print("PADRE: creando HIJO {0}".format(i))
    piscina.append(multiprocessing.Process(name="Proceso {0}".format(i), target=tarea(i).run))

# Arrancamos a todos los hijos
print("PADRE: arrancando hijos")
for proceso in piscina:
    proceso.start()

print("PADRE: esperando a que los procesos hijos hagan su trabajo")
# Mientras la piscina tenga procesos
while piscina:
    # Para cada proceso de la piscina
    for proceso in piscina:
        # Revisamos si el proceso ha muerto
        if not proceso.is_alive():
            # Recuperamos el proceso y lo sacamos de la piscina
            proceso.join()
            piscina.remove(proceso)
            del(proceso)

    # Para no saturar, dormimos al padre durante 1 segundo
    print("PADRE: esperando a que los procesos hijos hagan su trabajo")
    time.sleep(1)

print("PADRE: todos los hijos han terminado, cierro")
