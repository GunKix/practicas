#Ejercicios practica


#ejercicio 1, escibir yes para finalizar
pal:str=(input("Desea continuar el programa: "))
while (pal != "yes"):
    pal:str=(input("Desea continuar el programa: "))
print ("Programa finalizado")



#ejercicio 2, escribir cualquier cosa menos n para finalizar
pal1:str=(input("Desea terminar el programa: "))
while(pal1 == "n"):
    pal1:str=(input("Desea terminar el programa: "))
else:
    print("Terminando programa")
    
    
#ejercicio 3, esciribir cualquier cosa menos no para finalizar
pal2:str=(input("Desea terminar el programa: "))
while(pal2 == "no"):
    pal1:str=(input("Desea terminar el programa: "))
else:
    print("Terminando programa")
    
#ejercicio 4, confimar la contrasena     
con:str=(input("Escriba su contrasena: "))
con1:str=(input("Confirme su contrasena: "))
while(con == con1): 
    print("Su contrasena es correcta")
    break
else:
    print("Vuelva a intentarlo")
    

#ejercicio 5    
print("Hucha")
din=float(input("Cuanto quiere ahorrar: "))

ahorro:float = 0.0
while din > ahorro: 
    ahorro += float(input("Cuanto quiere abonar: "))
print("Felicidades usted ha ahorrado:", ahorro)



#ejercicio 6, poner la contrasena correcta y dar un limite de intentos

contra:str=(input("Escriba una contrasena: "))
intentos=3
print("Tiene 3 intentos para confirmar su contrasena")
contra1:str=(input("Confirme su contrasena: "))
contador=1

while(contra!=contra1 and contador < intentos):
    print("Esa no es la contrasena ")
    contra1:str=(input("Confirme su contrasena: "))
    contador+=1
    
if (contra==contra1):
    print("La contrasena es correcta")
else:
    print("Ya no quedan intentos")
    


  
    







        