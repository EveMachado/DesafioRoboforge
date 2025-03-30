from math import *

def detectar_tipo(dado_str):
    
    dado_str = dado_str.strip()  
   
    if dado_str.lower() == "true":
        return True, "bool"
    if dado_str.lower() == "false":
        return False, "bool"
 
    try:
        valor = int(dado_str)
        return valor, "int"
    except ValueError:
        pass
   
    try:
        valor = float(dado_str)
        return valor, "float"
    except ValueError:
        pass

    return dado_str, "str"

def ler_dado():
   
    dado_str = input("Digite um dado: ")
    valor, tipo = detectar_tipo(dado_str)
    print(f"Você digitou: {valor} e o tipo é {tipo}")

def ler_lista():
    
    n = int(input("Quantos dados você deseja inserir na lista? "))
    lista = []
    for i in range(n):
        dado_str = input(f"Digite o dado {i+1}: ")
        valor, _ = detectar_tipo(dado_str)
        lista.append(valor)
    print("Lista:", lista)
    return lista

def codificar_lista(lista):
    partes = []
    for item in lista:
    
        if isinstance(item, bool):
            tipo = "bool"
            representacao = f"(bool: {item})"
        elif isinstance(item, int):
            tipo = "int"
            representacao = f"(int: {item})"
        elif isinstance(item, float):
            tipo = "float"
            representacao = f"(float: {item})"
        elif isinstance(item, str):
            tipo = "str"
            representacao = f"(str: '{item}')"
        else:
            tipo = "str"
            representacao = f"(str: '{item}')"
        partes.append(representacao)
    codificado = ", ".join(partes)
    print("Lista codificada:")
    print(codificado)
    return codificado

def decodificar_lista(codificado):
   
    partes = codificado.split("), (")
    lista_decodificada = []
    
    for parte in partes:
      
        parte = parte.strip("()")
        tipo, valor_str = parte.split(": ", 1)
        
        if tipo == "int":
            valor = int(valor_str)
        elif tipo == "float":
            valor = float(valor_str)
        elif tipo == "bool":
            valor = True if valor_str.strip() == "True" else False
        else: 
            valor = valor_str.strip("'")
        
        lista_decodificada.append(valor)
    
    return lista_decodificada


def main():

    print("1: Verificar tipo do dado digitado")
    ler_dado()
    
    print("\n2: Ler uma lista de dados")
    lista = ler_lista()
    
    print("\n3: Codificar a lista em uma string")
    codificado = codificar_lista(lista)
    
    print("\n4: Decodificar a string para obter a lista")
    lista_decodificada = decodificar_lista(codificado) 
    print("Lista decodificada:", lista_decodificada)

if __name__ == "__main__":
    main()
