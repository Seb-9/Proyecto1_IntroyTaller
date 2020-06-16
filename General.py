def generar_val_llave(n):
    """

    La funcion generar_val_llave

    Parametros:
    n=es el numero inicial para iniciar la encriptacion con el metodo LSFR

    Retorna:
    Un numero semi-aleatorio dentro de 1 y 255
    """

    bits=[0,0,0,0,0,0,0,0] #se define un byte = 0(parte del LSFR)
    bits = C_Binario(n,bits)
    bits = Desplazamiento(((bits[7]^bits[5])^bits[3])^bits[2],bits,len(bits)-1)
    numb = num_bits(len(bits)-1,bits,0)
    return C_BaseDiez(numb,0)

def Desplazamiento(a,bits,indice):
    if indice==0:
        bits[0]=a
        return bits
    else:
        bits[indice]=bits[indice-1]
        return Desplazamiento(a,bits,indice-1)

def num_bits(largo,bits,r):
    if largo==0:
        return bits[largo]*(10**r)
    else:
        return (bits[largo]*(10**r))+num_bits(largo-1,bits,r+1)

def C_Binario(n,bits):
    num=aux_Binario(n,0,0)
    return aux_bits(num,bits,-1)

def aux_bits(num,bits,x):
    if num<10:
        bits[x]=num
        return bits
    else:
        bits[x]=num%10
        return aux_bits(num//10,bits,x-1)

def aux_Binario(n,p,r):
    if n<2:
        return r+(n*(10**p))
    else:
        if n%2==0:
            return aux_Binario(n//2,p+1,r+(0*(10**p)))
        else:
            return aux_Binario(n//2,p+1,r+(1*(10**p)))

def C_BaseDiez(n,p): #convierte el 
    if n<10:
        return n*(2**p)
    else:
        return ((n%10)*(2**p))+ C_BaseDiez(n//10,p+1)


palabras_encriptadas=[] # lista global para poder guardar cada palabra encriptada
llaves_palabras=[] # variable global para poder guardar las llaves correpondientes a cada letra de cada palabra
#estas dos listas practimente crean un diccionario, en el cual cada palabra encriptada es el id y los llaves su lista objeto

abc="abcdefghijklmnñopqrstuvwxyz" # se crea este string para poder localizar la posicion de cada letra
def encriptar(s,n):
    """
    La funcion encripta palabras

    Parametros:
    s = una palabra cualquiera
    n = un numero entre 1 y 255
    
    Retorna:
    La palabra(s) encriptada segun el numero(n) usando el metodo LSFR
    """
    
    llave= llaves(n,len(s),0,[])
    palabra= aux(s,len(s)-1,abc,llave,"",0,0)
    guardar(palabra,llave,0)
    return palabra

def llaves(n,largo,c,lista):
    if largo==c:
        return lista
    else:
        llave=generar_val_llave(n)# se envia a la funcion principal del LSFR para generar llaves
        if llave>27:
            lista.append(llave//27)
        else:
            lista.append(llave)
        return llaves(llave,largo,c+1,lista)

def aux(s,indice,abc,llaves,nueva_palabra,c,nuevaletra):
    if c>indice:
        return nueva_palabra
    else:
        nueva_letra= posicion_e(s[c],llaves[c]) #se llama a posicion_e para determinar la nueva letra
        nueva_palabra=nueva_palabra+abc[nueva_letra]
        return aux(s,indice,abc,llaves,nueva_palabra,c+1,0)
    
def posicion_e(letra,n):
    if 1+abc.index(letra)+n>=27: #no se le puede sumar a "z" un valor en su posicion, no existe, por lo que aqui se evalua
        return abc.index(letra)+n-27 #dara el indice exacto de la letra que se debe 
    else:
        return n+abc.index(letra)

def guardar(palabra,llaves,condicion):
    if condicion==0: # se guardan la palabra y las llaves de cada letra de esa palabra, para poder desencriptar
        palabras_encriptadas.append(palabra)
        llaves_palabras.append(llaves)
    if condicion==1: # aqui se solicitan las llaves de cada letra de la palabra encriptada
        posicion=palabras_encriptadas.index(palabra)
        return llaves_palabras[posicion]
        
def desencriptar(s,n):
    """

    La funcion desencripa palabras

    Parametros:
    s = una palabra cualquiera
    n = un numero entre 1 y 255

    Retorna:
    la palabra (s) ingresada desencriptada segun el numero(n) 

    """
    
    if n==0: #si se conoce una palabra encriptada pero no su "n"(codigo de encriptacion)
             #se puede ingresar aqui, para saber que significa, solo si se encripto antes
        llave=guardar(s,0,1) #se obtienen las llaves correspondientes a esa palabra
        return aux2(s,len(s)-1,abc,llave,"",0,0)
    else:
        llave=llaves(n,len(s),0,[])
        return aux2(s,len(s)-1,abc,llave,"",0,0)

def aux2(s,indice,abc,llaves,nueva_palabra,c,nuevaletra):
    if c>indice:
        return nueva_palabra
    else:
        nueva_letra= posicion_d(s[c],llaves[c]) #se llama a posicion_d para determinar la nueva letra
        nueva_palabra=nueva_palabra+abc[nueva_letra]
        return aux2(s,indice,abc,llaves,nueva_palabra,c+1,0)

def posicion_d(letra,n):
    return (abc.index(letra))-n

def mostrar_palabras_encriptadas():
    """

    La funcion muestra las palabras previamente encriptadas

    Parametros:
    No recibe

    Retorna:
    Una lista con todas la palabras ecriptadas
    """
    
    return palabras_encriptadas
