import random 
 
    # Método para obtener una lista con 18 pares de emojis ordenados de manera aleatoria
def randomizarEmojis() -> list:
    emojis = ['🌚', '😤', '🐸', '🐋', '🐧', '🦈', '🤠', '🦖', '🤡', '🌈', '🍑', '🙂', '🙃', '👻', '💀', '🥵', '👽', '🤖']
    listaRes = list()
     #Creamos una lista que va de 0 a 35 y la "revolvemos"
    lista = list(range(0,36))
    random.shuffle(lista)

        #para obtener cada par de emoji, convertimos los numeros mayores a 18 en sus complemetarios "usando la suma de Gauss" para 35. (35,0) (34,1) (33,2) ... (18,17).
    for i in lista:
        if i>17:
            #así: (35-35 = 0), (35 - 34 = 1), (35 - 33 = 2) ... (35 - 18 = 17).
            listaRes.append(emojis[35-i])
        else:
            listaRes.append(emojis[i])
    return listaRes