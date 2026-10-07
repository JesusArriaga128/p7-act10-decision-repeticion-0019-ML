
# ==============================================================================
# FUNCIONES: MÚLTIPLES EJEMPLOS DE CONTROL DE FLUJO Y BUCLES
# JESUS ARRIAGA NC=0019
# 2 ejemplos por cada caso, presentados secuencialmente mediante print()
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. PYTHON IF
# Ref: https://www.w3schools.com/python/python_conditions.asp
# ------------------------------------------------------------------------------
print("==================================================")
print(" 1. PYTHON IF")
print("==================================================")

# Ejemplo 1
print("\n--- Ejemplo 1: Verificación de edad ---")
edad = 20
print("Datos de entrada: edad =", edad)
if edad >= 18:
    print("Resultado: La persona es mayor de edad.")

# Ejemplo 2
print("\n--- Ejemplo 2: Evaluación de número positivo ---")
numero = 15
print("Datos de entrada: numero =", numero)
if numero > 0:
    print("Resultado: El número es positivo.")


# ------------------------------------------------------------------------------
# 2. PYTHON IF ... ELIF
# Ref: https://www.w3schools.com/python/python_if_elif.asp
# ------------------------------------------------------------------------------
print("\n==================================================")
print(" 2. PYTHON IF ... ELIF")
print("==================================================")

# Ejemplo 1
print("\n--- Ejemplo 1: Sistema de calificaciones ---")
nota = 85
print("Datos de entrada: nota =", nota)
if nota >= 90:
    print("Resultado: Calificación A (Excelente)")
elif nota >= 80:
    print("Resultado: Calificación B (Notable)")
elif nota >= 70:
    print("Resultado: Calificación C (Aprobado)")

# Ejemplo 2
print("\n--- Ejemplo 2: Etapas de crecimiento ---")
anios = 14
print("Datos de entrada: anios =", anios)
if anios < 2:
    print("Resultado: Categoria Bebé")
elif anios < 12:
    print("Resultado: Categoria Niño")
elif anios < 18:
    print("Resultado: Categoria Adolescente")


# ------------------------------------------------------------------------------
# 3. PYTHON IF ... ELSE
# Ref: https://www.w3schools.com/python/python_if_else.asp
# ------------------------------------------------------------------------------
print("\n==================================================")
print(" 3. PYTHON IF ... ELSE")
print("==================================================")

# Ejemplo 1
print("\n--- Ejemplo 1: Par o Impar ---")
numero_evaluar = 7
print("Datos de entrada: numero_evaluar =", numero_evaluar)
if numero_evaluar % 2 == 0:
    print("Resultado: El número es PAR.")
else:
    print("Resultado: El número es IMPAR.")

# Ejemplo 2
print("\n--- Ejemplo 2: Validación de clave ---")
clave_usuario = "12345"
print("Datos de entrada: clave_usuario =", clave_usuario)
if clave_usuario == "secret123":
    print("Resultado: Acceso concedido.")
else:
    print("Resultado: Acceso denegado.")


# ------------------------------------------------------------------------------
# 4. PYTHON FOR LOOPS
# Ref: https://www.w3schools.com/python/python_for_loops.asp
# ------------------------------------------------------------------------------
print("\n==================================================")
print(" 4. PYTHON FOR LOOPS")
print("==================================================")

# Ejemplo 1
print("\n--- Ejemplo 1: Recorrer lista de tecnologías ---")
lenguajes = ["Python", "JavaScript", "C++", "Java"]
print("Recorriendo la lista:")
for lenguaje in lenguajes:
    print(" - Lenguaje:", lenguaje)

# Ejemplo 2
print("\n--- Ejemplo 2: Bucle con range() (Tabla de multiplicar) ---")
print("Tabla del 5:")
for i in range(1, 6):
    print(" 5 x", i, "=", 5 * i)


# ------------------------------------------------------------------------------
# 5. PYTHON WHILE LOOPS
# Ref: https://www.w3schools.com/python/python_while_loops.asp
# ------------------------------------------------------------------------------
print("\n==================================================")
print(" 5. PYTHON WHILE LOOPS")
print("==================================================")

# Ejemplo 1
print("\n--- Ejemplo 1: Conteo decreciente ---")
contador = 5
print("Iniciando cuenta regresiva:")
while contador > 0:
    print(" Valor actual:", contador)
    contador = contador - 1
print("Fin de la cuenta.")

# Ejemplo 2
print("\n--- Ejemplo 2: Suma acumulativa ---")
suma = 0
paso = 1
print("Acumulando valores del 1 al 5:")
while paso <= 5:
    suma = suma + paso
    print(" Paso", paso, "| Suma actual:", suma)
    paso = paso + 1

print("\n==================================================")
print(" FIN DE LOS EJERCICIOS")
print("==================================================")

print("PROGRAMA REALIZADO POR JESUS ARRIAGA 0019")