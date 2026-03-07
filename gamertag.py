def cabecera():
    #Muestra la cabecera de la aplicación
    # con r se invalidan los \

    titulo = r"""
     \/          \\\    ///      ))   (o)__(o)        \/     oo_    
    (OO)     /)  ((O)  (O)) wWw (Oo)-.(__  __)/)     (OO)   /  _)-< 
  ,'.--.)  (o)(O) | \  / |  (O)_ | (_)) (  )(o)(O) ,'.--.)  \__ `.  
 / /|_|_\   //\\  ||\\//|| .' __)|  .'   )(  //\\ / /|_|_\     `. | 
 | \_.--.  |(__)| || \/ ||(  _)  )|\\   (  )|(__)|| \_.--.     _| | 
 '.   \) \ /,-. | ||    || `.__)(/  \)   )/ /,-. |'.   \) \ ,-'   | 
   `-.(_.'-'   ''(_/    \_)      )      (  -'   ''  `-.(_.'(_..--'  
                      🕹️¡Crea tu identidad gamer!🕹️
"""
    print(titulo)

#cabecera()


def crear_tag_basico(nombre):
    """
    
    Cra un gamer tag basico usando las primeras letras del nombre del usuario.
    Parámetro:
    nombre(str): El nombre del usuario

    Retorna:
    str: Gamertag básico

    """

    tag=nombre[0:4]

    return(tag)


#tag_basico = crear_tag_basico("Ricardo")
#print(tag_basico)

pass
def crear_tag_invertido(nombre):
    """
    Cra un gamertag invirtiendo el nombre completo
    Parámetro:
    nombre(str): El nombre del usuario

    Retorna:
    str: Gamertag (nombre)invertido

    """

    tag = nombre[::-1] 
    return tag


tag_ivertido=crear_tag_invertido("Ricardo")
print(tag_ivertido)

pass
def crear_tag_intercalado(nombre,apellido):
    inicial_nombre=nombre[0]
    inicial_apellido=apellido[0]
    resto_nombre=nombre[1:]
    resto_apellido=apellido[:1]

    print("3. TAG INTERCALADO: ", inicial_nombre,inicial_apellido,resto_nombre,resto_apellido,sep="")

crear_tag_intercalado("Ricardo","Godínez")

pass

def crear_tag_elite(nombre):

    inicio=nombre[:2]
    final=nombre[-2:]

    print("4. TAG ELITE: ", inicio, final, sep="")

crear_tag_elite("Santiago")

    #pass

def crear_tag_con_numero(nombre,numero_favorito):

    print("5, TAG CON NÚMERO: ", nombre[:5],numero_favorito, sep="")

crear_tag_con_numero("Ricardo",35)

pass

def mostrar_estadisticas(nombre):
    longitud_nombre=len(nombre)
    print("ESTADÍSTICAS DE TU NOMBRE:")
    print("Nombre completo:", nombre)
    print("Primera letra:",nombre[0])
    print("Ultima letra:",nombre[-1])



def generar_todas_opciones(nombre,apellido,numero):
    """
    Genera y muestra todas las opcines de gamertags
    Parámetros:
    nombre(str): Nombre del usuario
    apellido(str): Apellido del usuario
    número(str):

    Retorna:
    None(Imprime directamente
    """

    print("\n=================================")
    print("TUS OPCIONES DE GAMERTAG: ")
    print("=================================")


    tag_basico = crear_tag_basico(nombre)

    print("\n1. TAG BASICO:", tag_basico)
    print("2. TAG INVERTIDO",crear_tag_invertido(nombre))
    crear_tag_intercalado(nombre, apellido)
    crear_tag_elite(nombre)
    crear_tag_con_numero(nombre, numero)


    print("\n====================================")




#------------------------------------------------
#APLICACIÓN PRINCIPAL
#-----------------------------------------------
#llamar a la función cabecera


cabecera()

#solicitar datos del usuario

nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
numero=input("Introduce tu número favorito:")



#Mostrar estadisticas del nombre


mostrar_estadisticas(nombre)
generar_todas_opciones("Ricardo", "Godinez", 35)


print("\n🕹️ ¡Elige tu favorito y conquista el mundo gamer! 🕹️ \n ")


      



    


    









