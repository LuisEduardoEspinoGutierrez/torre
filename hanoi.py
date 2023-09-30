

def  Torre (bloques,inicio,intermedio,final):

    if bloques ==  1:
        return 1
    else:
        Torre(bloques-1,inicio,final,intermedio)
        print("el bloque",bloques,"se movio de ",inicio,"hasta ",final)
        Torre(bloques-1,intermedio,inicio,final)

bloques= int(input('cuantos bloques quiere en la torre: '))
            
if bloques > 7:
    print('solo se permiten hasta 7 bloques')
else:
    Torre(bloques,'t1','t2','t3')
                
