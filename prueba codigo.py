import math

def get_cuadrado(numero):
    try:
        numero = int(numero)
    except ValueError:
        raise HTTPException(status_code=400, detail="Argumento no válido. El valor proporcionado debe ser un número entero")
    else:
        intentos = 0
        while numero < 0:
            print("No se puede hallar la raíz cuadrada de un número negativo.")
            intentos += 1
        if intentos >= 2:
            print("Has consumido demasiados intentos. El programa ha finalizado")
            raise HTTPException(status_code=400, detail="Demasiados intentos. El programa ha finalizado")

    solucion = math.sqrt(numero)
    resultado = f"La raíz cuadrada de {numero} es: {solucion}"

    return {"resultado": resultado}

print(get_cuadrado(12))
