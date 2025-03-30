from math import sqrt, acos, degrees, isclose

def ler_pontos():

    pontos = []
    for i in range(3):
        x = float(input(f"Digite a coordenada X do ponto {i + 1}: "))
        y = float(input(f"Digite a coordenada Y do ponto {i + 1}: "))
        pontos.append((x, y))
    return pontos

def calcular_lados(pontos):
   
    A, B, C = pontos
    """" formula da distancia entre pontos: d = sqrt((x2-x1)^2 + (y1-y2)^2)"""
    a = sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    b = sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)
    c = sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    return a, b, c

def calcular_angulos(a, b, c):
    """lei dos cossenos"""
    """função inversa do cosseno (acos) para encontra os angulos atraves de radianos"""
    """degrees() = converter em graus"""
    angleA = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angleB = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angleC = degrees(acos((a**2 + b**2 - c**2) / (2 * a * b)))
    return angleA, angleB, angleC

def calcular_perimetro(a, b, c):

    return a + b + c

def calcular_area(a, b, c):
   
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

def classificar_lados(a, b, c):
 
    if isclose(a, b) and isclose(b, c):
        return "Equilátero"
    elif isclose(a, b) or isclose(b, c) or isclose(a, c):
        return "Isósceles"
    else:
        return "Escaleno"

def classificar_angulos(angleA, angleB, angleC):
  
    if isclose(angleA, 90, abs_tol=1e-1) or isclose(angleB, 90, abs_tol=1e-1) or isclose(angleC, 90, abs_tol=1e-1):
        return "Retângulo"
    elif angleA > 90 or angleB > 90 or angleC > 90:
        return "Obtusângulo"
    else:
        return "Acutângulo"

def main():
  
    print("Informe as coordenadas dos 3 pontos do triângulo:")
    pontos = ler_pontos()

    a, b, c = calcular_lados(pontos)
    print("\nLados do triângulo:")
    print(f"a = {a:.2f}")
    print(f"b = {b:.2f}")
    print(f"c = {c:.2f}")

    angleA, angleB, angleC = calcular_angulos(a, b, c)
    print("\nÂngulos do triângulo (em graus):")
    print(f"Ângulo A = {angleA:.2f}")
    print(f"Ângulo B = {angleB:.2f}")
    print(f"Ângulo C = {angleC:.2f}")

    perimetro = calcular_perimetro(a, b, c)
    area = calcular_area(a, b, c)
    print("\nPerímetro e Área:")
    print(f"Perímetro = {perimetro:.2f}")
    print(f"Área = {area:.2f}")

    tipo_lados = classificar_lados(a, b, c)
    tipo_angulos = classificar_angulos(angleA, angleB, angleC)
    print("\nClassificação do triângulo:")
    print(f"Lados: {tipo_lados}")
    print(f"Ângulos: {tipo_angulos}")

if __name__ == "__main__":
    main()
