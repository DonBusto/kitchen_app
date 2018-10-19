import numpy as np
import datetime
import time
import cv2
import os

cap = cv2.VideoCapture(0) #Cap coge la webcam. En caso de tener muchas webcams conectadas ira por orden de prioridad. VideoCapture(0)
#indica que la webcam que se va a utilizar va a ser la que se haya establecido como dispositivo principal de captura de vídeo.
pesofinal = [] #Lista temporal de floats a comparar
pesofinal.append(0) #Para que la lista temporal que compara floats funcione desde el primer momento.
while True: #Codigo para que el programa sea fijo y nunca acabe.

    datovalido2 = False #El dato válido se da cuando se introduce un float mayor que 0, para que la bascula empiece a pesar
    i = 0
    peso = input("Peso: ")
    while datovalido2 == False: #Realizamos la funcion replace porque la bascula por defecto escribe los numeros con un
        #simbolo de igual, unos cuantos numeros delante y una coma, que se ha de cambiar por un punto para que
        #Python lo coja como float
        try:
            peso = peso.replace(",", ".")
            peso = peso.replace(".", "")
            peso = peso.replace("=", "")
            peso = float(peso)
            if peso != 0:
              datovalido2 = True
        except: #Lo comentado previamente. Datovalido se activara cuando se meta un producto que pese mas que cero
            #y entonces comenzara el pesaje
            print("Peso no ha sido reconocido como float o es igual a 0.")
            peso = input("Peso:")

    if peso != 0:
        #Puede que lo que pesemos le parezca a la bascula que pese mas porque nosotros tenemos la mano encima de lo que
        #vayamos a pesar. Para evitarlo, cogemos diez valores e imprimimos el mas comun de los diez, que sera logicamente
        #el peso real de nuestra comida
        listapesos = []
        for i in range(0,10):
            inputpeso = input("Peso de la comida: ")
            try: #realizamos la funcion replace y quitamos los dos primeros numeros, que al ser valores
                #que no se corresponden con el peso, no nos interesan
                inputpeso = inputpeso.replace(",", ".")
                inputpeso = inputpeso.replace("=","")
                inputpeso = inputpeso[2:]
                inputpeso = float(inputpeso)
                listapesos.append(inputpeso)
            except:
                i -= 1
        floatpeso = float(max(set(listapesos), key=listapesos.count)) #printea el valor mas comun de la lista
        pesofinal.append(floatpeso) #anyadimos a la lista de floats
        print(pesofinal)
        if pesofinal[len(pesofinal)-1] == pesofinal[len(pesofinal)-2]: #comparamos la lista de floats de peso
            #No nos interesa que un articulo sea pesado x veces porque lleve mucho tiempo puesto en la bascula
            #Como el programa es automatizado, el pesaje nunca acabara, y esto evita que se saquen muchas fotos
            #del mismo producto y que se guarden los pesos en el log
            del pesofinal[len(pesofinal)-1]
            print ("El peso es el mismo que el anterior. No se guardara la imagen.")
        else:
            print("El peso de la comida es de %.3f kg" % floatpeso)
            fichero = open("home/pi/kitchen_app/pesos.log", "a") #editamos el log que tiene el historial de pesajes
            fichero.write("Peso: %.3f medido el " % floatpeso)
            fichero.write("%s" % (datetime.datetime.now()))
            fichero.write("\n")
            fichero.close()
          #  cap = cv2.VideoCapture(0)
            ret,frame = cap.read()
            print(ret)
            #cv2.imwrite(("C:/Users/Usuario/Desktop/pyCharm/%s.jpg" % (datetime.datetime.now())),frame)
            hora = time.time()
            try:
                cv2.imwrite(("home/pi/kitchen_app/%s.jpg" % (hora)), frame) #guarda la imagen, que al ser guardada con el
                #formato de la hora, sabemos que no se va a sobreescribir ningun archivo porque el tiempo avanza en una
                #sola direccion
            except:
                print("Se ha creado la imagen igualmente")
            fichero = open("home/pi/kitchen_app/pesos.log", "a")
            fichero.write("Ruta absoluta de la imagen: %s\n\n" % (os.path.abspath(("%s.jpg" % (hora)))))
            #cogemos la ruta absoluta de la imagen para ponerla en el log una vez guardada la foto
            fichero.close()
            del pesofinal[(len(pesofinal)-2)]
            print(pesofinal)
           # cv2.waitKey() --esto era una prueba a secas
            cv2.destroyAllWindows()

