import random


def e_primo(numero):
  
    if numero < 2:
        return False  

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  

    return True  

def gerar_lista():
    inicio = random.randint(1, 50)
    fim = random.randint(inicio + 10, inicio + 50)
    lista = (random.sample(range(inicio, fim + 1), 10)) 
    return lista 

def multiplicar_primos(lista):
    primos = [num for num in lista if e_primo(num)]
    if not primos:  
        return 0
    resultado = 1
    for p in primos:
        resultado *= p
    return resultado

lista_numeros = gerar_lista()
print("Lista gerada:", lista_numeros)

resultado = multiplicar_primos(lista_numeros)
print("Multiplicação dos primos:", resultado)

