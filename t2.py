def columnar_transposition(key, message):
    # Eliminar espacios en el mensaje
    message = message.upper().replace(" ", "")

    # Agregar caracteres de relleno si la longitud del mensaje no es un múltiplo de la longitud de la clave
    while len(message) % len(key) != 0:
        message += " "

    # Crear la matriz de caracteres
    matrix = []
    for i in range(0, len(message), len(key)):
        row = list(message[i:i+len(key)])
        matrix.append(row)

    # Ordenar las columnas de la matriz según la clave
    sorted_columns = sorted(range(len(key)), key=lambda k: key[k])

    # Concatenar los caracteres de las columnas ordenadas para formar el mensaje cifrado
    encrypted_message = ""
    for i in sorted_columns:
        for row in matrix:
            encrypted_message += row[i]

    return encrypted_message

# Pedir la clave y el mensaje al usuario
clave = input("Introduce la clave: ")
mensaje = input("Introduce el mensaje a cifrar: ")

# Cifrar el mensaje con la clave dada
mensaje_cifrado = columnar_transposition(clave.upper().replace(" ", ""), mensaje)

# Imprimir el mensaje cifrado
print("Mensaje cifrado: " + mensaje_cifrado)
